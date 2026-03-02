class InputParser:
    def __init__(self, minimum, maximum):
        self._minimum = minimum
        self._maximum = maximum

    def parse(self, text, parameter_name):
        value = self._parse_integer(text, parameter_name)
        if value < self._minimum or value > self._maximum:
            raise ValueError(
                f"{parameter_name} must be between "
                f"{self._minimum} and {self._maximum}.")
        return value

    @staticmethod
    def _parse_integer(text, parameter_name):
        try:
            value = int(text)
            if value <= 0:
                raise ValueError(
                    f"{parameter_name} must be a positive integer.")
            return value
        except ValueError as error:
            if "positive integer" in str(error):
                raise
            raise ValueError(
                f"'{text}' is not a valid integer for {parameter_name}.")