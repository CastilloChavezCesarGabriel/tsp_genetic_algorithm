from model.visitors.route_visitor import RouteVisitor
from tests.counter_verifier import CounterVerifier


class MockRouteVisitor(RouteVisitor, CounterVerifier):
    def __init__(self, test_case, expected_count):
        CounterVerifier.__init__(self, test_case, expected_count)

    def traverse(self, origin, destination):
        self._increment()
