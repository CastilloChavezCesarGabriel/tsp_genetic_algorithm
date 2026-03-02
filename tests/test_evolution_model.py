import unittest
from model.evolution_model import EvolutionModel
from tests.mock_observer import MockObserver
from tests.mock_evolution_visitor import MockEvolutionVisitor


class TestEvolutionModel(unittest.TestCase):
    def _create_initialized_model(self):
        model = EvolutionModel()
        model.initialize(800.0, 600.0)
        model.reset(20)
        return model

    def test_initialize_creates_population(self):
        model = self._create_initialized_model()
        visitor = MockEvolutionVisitor(self)
        model.accept(visitor)
        visitor.verify_route_exists()

    def test_step_advances_generation(self):
        model = self._create_initialized_model()
        observer = MockObserver(self)
        model.register(observer)
        model.step()
        observer.verify_generations(1)

    def test_step_preserves_city_count(self):
        model = self._create_initialized_model()
        model.step()
        visitor = MockEvolutionVisitor(self)
        model.accept(visitor)
        visitor.verify_city_count(20)

    def test_observer_notified_on_completion(self):
        model = self._create_initialized_model()
        observer = MockObserver(self)
        model.register(observer)
        for _ in range(500):
            model.step()
        observer.verify_completed()

    def test_reset_regenerates_population(self):
        model = self._create_initialized_model()
        model.step()
        observer = MockObserver(self)
        model.register(observer)
        model.reset(20)
        observer.verify_generations(1)

    def test_reset_changes_city_count(self):
        model = self._create_initialized_model()
        model.reset(10)
        visitor = MockEvolutionVisitor(self)
        model.accept(visitor)
        visitor.verify_city_count(10)


if __name__ == "__main__":
    unittest.main()
