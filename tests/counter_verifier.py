class CounterVerifier:
    def __init__(self, test_case, expected_count):
        self._test_case = test_case
        self._expected_count = expected_count
        self._current_count = 0

    def _increment(self):
        self._current_count += 1

    def verify(self):
        self._test_case.assertEqual(
            self._current_count, self._expected_count
        )
