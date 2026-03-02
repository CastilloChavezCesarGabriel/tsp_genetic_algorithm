from abc import ABC, abstractmethod

class EvolutionVisitor(ABC):
    @abstractmethod
    def visit_statistics(self, generation: int, best_distance: float) -> None:
        pass

    @abstractmethod
    def visit_best_route(self, route) -> None:
        pass