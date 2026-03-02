import random
from model.factories.city_factory import CityFactory
from model.observers.evolution_observer import EvolutionObserver
from model.factories.route_factory import RouteFactory
from model.visitors.evolution_visitor import EvolutionVisitor

class EvolutionModel:
    _DEFAULT_GENERATION_LIMIT = 500
    _TOURNAMENT_SIZE = 3
    _PADDING = 30

    def __init__(self):
        self._current_generation = 0
        self._routes = []
        self._observers = []
        self._city_factory = None
        self._route_factory = RouteFactory(10)
        self._city_count = 0

    def register(self, observer: EvolutionObserver) -> None:
        self._observers.append(observer)

    def initialize(self, width: float, height: float) -> None:
        self._city_factory = CityFactory(self._PADDING, (width, height))

    def step(self) -> None:
        self._evolve()
        self._current_generation += 1
        self._notify(lambda observer: observer.on_generation_evolved())
        if self._current_generation >= self._DEFAULT_GENERATION_LIMIT:
            self._notify(lambda observer: observer.on_evolution_completed())

    def prepare(self, city_count: int) -> None:
        if not self._routes:
            self.reset(city_count)
            return
        if city_count != self._city_count:
            raise ValueError(
                "Press Reset to change the number of cities."
            )

    def reset(self, city_count: int) -> None:
        self._city_count = city_count
        self._current_generation = 0
        cities = self._city_factory.scatter(city_count)
        self._routes = self._route_factory.populate(cities)
        self._rank()
        self._notify(lambda observer: observer.on_generation_evolved())

    def accept(self, visitor: EvolutionVisitor) -> None:
        if self._routes:
            best = self._routes[0]
            visitor.visit_statistics(self._current_generation, best.evaluate())
            visitor.visit_best_route(best)

    def _evolve(self) -> None:
        elite = self._routes[0]
        new_routes = [elite]
        for _ in range(len(self._routes) - 1):
            parent = self._select()
            partner = self._select()
            child = parent.cross(partner)
            mutated = child.mutate()
            new_routes.append(mutated)
        self._routes = new_routes
        self._rank()

    def _select(self):
        candidates = random.sample(self._routes, self._TOURNAMENT_SIZE)
        return min(candidates, key=lambda route: route.evaluate())

    def _rank(self) -> None:
        self._routes.sort(key=lambda route: route.evaluate())

    def _notify(self, action) -> None:
        for observer in self._observers:
            action(observer)