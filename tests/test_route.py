import unittest
from model.city import City
from model.route import Route
from tests.mock_route_visitor import MockRouteVisitor
from tests.city_counter import CityCounter
from tests.city_identity_collector import CityIdentityCollector
from tests.destination_verifier import DestinationVerifier


class TestRoute(unittest.TestCase):
    def _create_cities(self):
        return [City(index, index) for index in range(5)]

    def _cross(self, cities):
        parent = Route(cities)
        partner = Route(list(reversed(cities)))
        return parent.cross(partner)

    def test_accept_visits_all_segments(self):
        cities = [City(0, 0), City(1, 1), City(2, 2)]
        route = Route(cities)
        visitor = MockRouteVisitor(self, 3)
        route.accept_route(visitor)
        visitor.verify()

    def test_accept_wraps_around_to_start(self):
        first_city = City(0, 0)
        route = Route([first_city, City(1, 1)])
        verifier = DestinationVerifier(self, first_city)
        route.accept_route(verifier)
        verifier.verify()

    def test_accept_city_visits_all_cities(self):
        cities = [City(0, 0), City(1, 1), City(2, 2)]
        route = Route(cities)
        counter = CityCounter(self, 3)
        route.accept_city(counter)
        counter.verify()

    def test_evaluate_computes_round_trip_distance(self):
        origin = City(0.0, 0.0)
        destination = City(3.0, 4.0)
        route = Route([origin, destination])
        self.assertAlmostEqual(route.evaluate(), 10.0)

    def test_evaluate_caches_distance(self):
        route = Route([City(0, 0), City(3, 4)])
        first_call = route.evaluate()
        second_call = route.evaluate()
        self.assertEqual(first_call, second_call)

    def test_evaluate_single_city_is_zero(self):
        route = Route([City(5.0, 5.0)])
        self.assertEqual(route.evaluate(), 0.0)

    def test_cross_produces_same_city_count(self):
        child = self._cross(self._create_cities())
        counter = CityCounter(self, 5)
        child.accept_city(counter)
        counter.verify()

    def test_cross_preserves_all_city_identities(self):
        cities = self._create_cities()
        original_identities = {id(city) for city in cities}
        child = self._cross(cities)
        collector = CityIdentityCollector(self, original_identities)
        child.accept_route(collector)
        collector.verify_subset()

    def test_cross_has_no_duplicate_cities(self):
        cities = self._create_cities()
        original_identities = {id(city) for city in cities}
        child = self._cross(cities)
        collector = CityIdentityCollector(self, original_identities)
        child.accept_route(collector)
        collector.verify_unique_count(5)

    def test_mutate_preserves_city_count(self):
        route = Route(self._create_cities())
        mutated = route.mutate()
        counter = CityCounter(self, 5)
        mutated.accept_city(counter)
        counter.verify()

    def test_mutate_preserves_all_city_identities(self):
        cities = self._create_cities()
        original_identities = {id(city) for city in cities}
        route = Route(cities)
        mutated = route.mutate()
        collector = CityIdentityCollector(self, original_identities)
        mutated.accept_route(collector)
        collector.verify_subset()


if __name__ == "__main__":
    unittest.main()
