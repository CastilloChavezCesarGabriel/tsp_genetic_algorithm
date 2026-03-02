import unittest
from model.city import City
from tests.mock_city_visitor import MockCityVisitor


class TestCity(unittest.TestCase):
    def test_accept_visits_coordinates(self):
        city = City(100.0, 200.0)
        visitor = MockCityVisitor(self, (100.0, 200.0))
        city.accept(visitor)

    def test_measure_distance_between_identical_cities_is_zero(self):
        city = City(50.0, 50.0)
        duplicate = City(50.0, 50.0)
        self.assertEqual(city.measure_distance(duplicate), 0.0)

    def test_measure_distance_computes_euclidean(self):
        origin = City(0.0, 0.0)
        destination = City(3.0, 4.0)
        self.assertAlmostEqual(origin.measure_distance(destination), 5.0)

    def test_measure_distance_is_symmetric(self):
        first = City(10.0, 20.0)
        second = City(30.0, 40.0)
        self.assertAlmostEqual(
            first.measure_distance(second),
            second.measure_distance(first)
        )


if __name__ == "__main__":
    unittest.main()
