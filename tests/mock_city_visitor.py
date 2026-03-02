from model.visitors.city_visitor import CityVisitor


class MockCityVisitor(CityVisitor):
    def __init__(self, test_case, expected_coordinate):
        self._test_case = test_case
        self._expected_coordinate = expected_coordinate

    def visit(self, horizontal, vertical):
        self._test_case.assertEqual(
            (horizontal, vertical), self._expected_coordinate
        )
