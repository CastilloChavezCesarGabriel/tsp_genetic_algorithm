from model.visitors.route_visitor import RouteVisitor


class DestinationVerifier(RouteVisitor):
    def __init__(self, test_case, expected_destination):
        self._test_case = test_case
        self._expected_destination = expected_destination
        self._last_destination = None

    def traverse(self, origin, destination):
        self._last_destination = destination

    def verify(self):
        self._test_case.assertIs(
            self._last_destination, self._expected_destination
        )
