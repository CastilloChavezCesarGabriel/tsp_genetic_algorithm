import random
from model.city import City

class CityFactory:
    def __init__(self, padding, dimensions):
        self._padding = padding
        self._dimensions = dimensions

    def scatter(self, city_count):
        width, height = self._dimensions
        return [
            City(
                random.uniform(self._padding, width - self._padding),
                random.uniform(self._padding, height - self._padding))
            for _ in range(city_count)]