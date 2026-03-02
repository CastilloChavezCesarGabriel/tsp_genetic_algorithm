from abc import ABC, abstractmethod

class EvolutionObserver(ABC):
    @abstractmethod
    def on_generation_evolved(self) -> None:
        pass

    @abstractmethod
    def on_evolution_completed(self) -> None:
        pass