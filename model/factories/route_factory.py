import random
from model.route import Route

class RouteFactory:
    def __init__(self, population_size):
        self._population_size = population_size

    def populate(self, cities):
        return [
            self._shuffle(cities)
            for _ in range(self._population_size)]

    @staticmethod
    def _shuffle(cities):
        shuffled = list(cities)
        random.shuffle(shuffled)
        return Route(shuffled)