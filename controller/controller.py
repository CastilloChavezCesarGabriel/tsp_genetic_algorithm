from controller.route_renderer import RouteRenderer
from controller.summary_visitor import SummaryVisitor
from model.observers.evolution_observer import EvolutionObserver
from model.visitors.city_visitor import CityVisitor
from model.visitors.evolution_visitor import EvolutionVisitor
from validation.input_parser import InputParser

class Controller(EvolutionObserver, EvolutionVisitor, CityVisitor):
    _TICK_DELAY = 50

    def __init__(self, model, view):
        self._model = model
        self._view = view
        self._schedule_identifier = None
        self._running = False
        self._city_count = 0
        self._model.register(self)
        self._view.register(self)

    def initialize(self) -> None:
        self._view.accept_dimensions(self)

    def receive_dimensions(self, width: float, height: float) -> None:
        self._model.initialize(width, height)

    def receive_count(self, text: str) -> None:
        self._city_count = InputParser(5, 30).parse(text, "City count")

    def on_generation_evolved(self) -> None:
        self._render()

    def on_evolution_completed(self) -> None:
        self._running = False
        self._cancel_loop()
        self._view.complete()
        self._render()
        self._model.accept(SummaryVisitor(self._view))

    def on_start_requested(self) -> None:
        if not self._validate_count():
            return
        try:
            self._model.prepare(self._city_count)
        except ValueError as error:
            self._view.warn(str(error))
            self._view.enable_start()
            return
        self._running = True
        self._view.enable_stop()
        self._loop()

    def on_stop_requested(self) -> None:
        self._stop()

    def on_reset_requested(self) -> None:
        self._stop()
        self._view.disable_reset()
        if not self._validate_count():
            return
        self._model.reset(self._city_count)
        self._view.reset_statistics()

    def visit(self, horizontal: float, vertical: float) -> None:
        self._view.place(horizontal, vertical)

    def visit_statistics(self, generation: int, best_distance: float) -> None:
        self._view.update_statistics(generation, best_distance)

    def visit_best_route(self, route) -> None:
        route_renderer = RouteRenderer(self._view)
        route.accept_route(route_renderer)
        route.accept_city(self)

    def _validate_count(self) -> bool:
        try:
            self._view.accept_count(self)
            return True
        except ValueError as error:
            self._view.warn(str(error))
            return False

    def _stop(self) -> None:
        self._running = False
        self._cancel_loop()
        self._view.enable_start()

    def _loop(self) -> None:
        self._model.step()
        if self._running:
            self._schedule_identifier = self._view.schedule(
                self._TICK_DELAY, self._loop
            )

    def _cancel_loop(self) -> None:
        if self._schedule_identifier is not None:
            self._view.cancel_schedule(self._schedule_identifier)
            self._schedule_identifier = None

    def _render(self) -> None:
        self._view.clear()
        self._model.accept(self)