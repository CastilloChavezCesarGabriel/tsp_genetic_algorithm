import tkinter as tk
from tkinter import messagebox
from view.map_canvas import MapCanvas
from view.control_panel import ControlPanel
from view.factories.widget_abstract_factory import WidgetAbstractFactory

class View:
    _CANVAS_WIDTH = 800
    _CANVAS_HEIGHT = 600
    _WINDOW_TITLE = "TSP - Genetic Algorithm"
    _BACKGROUND = "#2C3E50"
    _DEFAULT_STATISTICS = "Generation: 0  |  Best Distance: \u2014"

    def __init__(self, root: tk.Tk):
        root.title(self._WINDOW_TITLE)
        root.configure(bg=self._BACKGROUND)
        root.resizable(False, False)
        factory = WidgetAbstractFactory(root)
        self._controls = ControlPanel(root, factory)
        frame = factory.create_frame(root)
        self._statistics_label = factory.create_statistics_label(
            frame, self._DEFAULT_STATISTICS)
        self._canvas = MapCanvas(root, (self._CANVAS_WIDTH, self._CANVAS_HEIGHT))

    def register(self, listener) -> None:
        self._controls.register(listener)

    def clear(self) -> None:
        self._canvas.clear()

    def place(self, horizontal: float, vertical: float) -> None:
        self._canvas.place(horizontal, vertical)

    def connect(self, origin, destination) -> None:
        self._canvas.connect(origin, destination)

    def update_statistics(self, generation: int, distance: float) -> None:
        self._statistics_label.config(
            text=f"Generation: {generation}  |  Best Distance: {distance:.2f}"
        )

    def enable_start(self) -> None:
        self._controls.enable_start()

    def enable_stop(self) -> None:
        self._controls.enable_stop()

    def complete(self) -> None:
        self._controls.complete()

    def disable_reset(self) -> None:
        self._controls.disable_reset()

    def reset_statistics(self) -> None:
        self._statistics_label.config(text=self._DEFAULT_STATISTICS)

    def accept_dimensions(self, receiver) -> None:
        self._canvas.accept_dimensions(receiver)

    def accept_count(self, receiver) -> None:
        self._controls.accept_count(receiver)

    def schedule(self, delay: int, callback) -> str:
        return self._canvas.schedule(delay, callback)

    def cancel_schedule(self, schedule_identifier: str) -> None:
        self._canvas.cancel_schedule(schedule_identifier)

    @staticmethod
    def warn(message: str) -> None:
        messagebox.showerror("Validation Error", message)
