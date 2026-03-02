from model.observers.evolution_observer import EvolutionObserver


class MockObserver(EvolutionObserver):
    def __init__(self, test_case):
        self._test_case = test_case
        self._generations_evolved = 0
        self._completed = False

    def on_generation_evolved(self):
        self._generations_evolved += 1

    def on_evolution_completed(self):
        self._completed = True

    def verify_generations(self, expected_count):
        self._test_case.assertEqual(
            self._generations_evolved, expected_count
        )

    def verify_completed(self):
        self._test_case.assertTrue(self._completed)
