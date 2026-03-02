from model.visitors.route_visitor import RouteVisitor


class CityIdentityCollector(RouteVisitor):
    def __init__(self, test_case, expected_identities):
        self._test_case = test_case
        self._expected_identities = expected_identities
        self._collected = set()

    def traverse(self, origin, destination):
        self._collected.add(id(origin))
        self._collected.add(id(destination))

    def verify_subset(self):
        self._test_case.assertTrue(
            self._collected.issubset(self._expected_identities)
        )

    def verify_unique_count(self, expected_count):
        self._test_case.assertEqual(len(self._collected), expected_count)
