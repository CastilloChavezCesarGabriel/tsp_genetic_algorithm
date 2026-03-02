from abc import ABC, abstractmethod

class RouteVisitor(ABC):
    @abstractmethod
    def traverse(self, origin, destination) -> None:
        pass