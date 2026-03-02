from model.visitors.city_visitor import CityVisitor
from model.visitors.route_visitor import RouteVisitor

class RouteRenderer(RouteVisitor, CityVisitor):
    def __init__(self, view):
        self._view = view
        self._origin = None
        self._collecting_origin = True

    def traverse(self, origin, destination) -> None:
        self._collecting_origin = True
        origin.accept(self)
        self._collecting_origin = False
        destination.accept(self)

    def visit(self, horizontal: float, vertical: float) -> None:
        if self._collecting_origin:
            self._origin = (horizontal, vertical)
        else:
            self._view.connect(self._origin, (horizontal, vertical))