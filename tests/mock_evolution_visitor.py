from model.visitors.city_visitor import CityVisitor
from model.visitors.evolution_visitor import EvolutionVisitor


class MockEvolutionVisitor(EvolutionVisitor, CityVisitor):
    def __init__(self, test_case):
        self._test_case = test_case
        self._city_count = 0

    def visit_statistics(self, generation, best_distance):
        pass

    def visit_best_route(self, route):
        self._city_count = 0
        route.accept_city(self)

    def visit(self, horizontal, vertical):
        self._city_count += 1

    def verify_route_exists(self):
        self._test_case.assertGreater(self._city_count, 0)

    def verify_city_count(self, expected_count):
        self._test_case.assertEqual(self._city_count, expected_count)
