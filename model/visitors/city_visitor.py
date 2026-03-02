from abc import ABC, abstractmethod

class CityVisitor(ABC):
    @abstractmethod
    def visit(self, horizontal: float, vertical: float) -> None:
        pass