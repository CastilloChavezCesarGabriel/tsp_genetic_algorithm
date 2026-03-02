import random
from model.visitors.city_visitor import CityVisitor
from model.visitors.route_visitor import RouteVisitor

class Route:
    _MUTATION_RATE = 0.05

    def __init__(self, cities: list):
        self._cities = list(cities)
        self._distance = None

    def accept_route(self, visitor: RouteVisitor) -> None:
        for origin, destination in self._pair():
            visitor.traverse(origin, destination)

    def accept_city(self, visitor: CityVisitor) -> None:
        for city in self._cities:
            city.accept(visitor)

    def evaluate(self) -> float:
        if self._distance is not None:
            return self._distance
        total = 0.0
        for origin, destination in self._pair():
            total += origin.measure_distance(destination)
        self._distance = total
        return self._distance

    def _pair(self) -> list:
        return [
            (self._cities[index], self._cities[(index + 1) % len(self._cities)])
            for index in range(len(self._cities))
        ]

    def cross(self, partner: 'Route') -> 'Route':
        size = len(self._cities)
        child_cities = [None] * size
        inherited = set()
        start_index = random.randint(0, size - 2)
        end_index = random.randint(start_index + 1, size - 1)

        for position in range(start_index, end_index + 1):
            child_cities[position] = self._cities[position]
            inherited.add(id(self._cities[position]))

        fill_position = (end_index + 1) % size

        for city in partner._cities:
            if id(city) not in inherited:
                child_cities[fill_position] = city
                fill_position = (fill_position + 1) % size

        return Route(child_cities)

    def mutate(self) -> 'Route':
        if random.random() >= self._MUTATION_RATE:
            return Route(self._cities)

        mutated_cities = list(self._cities)
        first_index = random.randint(0, len(mutated_cities) - 1)
        second_index = random.randint(0, len(mutated_cities) - 1)

        while second_index == first_index:
            second_index = random.randint(0, len(mutated_cities) - 1)
        mutated_cities[first_index], mutated_cities[second_index] = (
            mutated_cities[second_index], mutated_cities[first_index])

        return Route(mutated_cities)