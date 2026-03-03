from model.visitors.city_visitor import CityVisitor

class City:
    def __init__(self, horizontal: float, vertical: float):
        self._horizontal = horizontal
        self._vertical = vertical

    def accept(self, visitor: CityVisitor) -> None:
        visitor.visit(self._horizontal, self._vertical)

    def measure_distance(self, destination: 'City') -> float:
        horizontal_axis_difference = destination._horizontal - self._horizontal
        vertical_axis_difference = destination._vertical - self._vertical
        return (horizontal_axis_difference ** 2 + vertical_axis_difference ** 2) ** 0.5