from model.visitors.city_visitor import CityVisitor
from tests.counter_verifier import CounterVerifier


class CityCounter(CityVisitor, CounterVerifier):
    def __init__(self, test_case, expected_count):
        CounterVerifier.__init__(self, test_case, expected_count)

    def visit(self, horizontal, vertical):
        self._increment()
