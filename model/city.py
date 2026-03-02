from model.visitors.city_visitor import CityVisitor

class City:
    def __init__(self, horizontal: float, vertical: float):
        self._horizontal = horizontal
        self._vertical = vertical

    def accept(self, visitor: CityVisitor) -> None:
        visitor.visit(self._horizontal, self._vertical)

    def measure_distance(self, destination: 'City') -> float:
        horizontal_delta = destination._horizontal - self._horizontal
        vertical_delta = destination._vertical - self._vertical
        return (horizontal_delta ** 2 + vertical_delta ** 2) ** 0.5