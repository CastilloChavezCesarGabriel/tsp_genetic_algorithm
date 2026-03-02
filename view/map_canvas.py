import tkinter as tk

class MapCanvas:
    _CITY_RADIUS = 5
    _CITY_COLOR = "#E74C3C"
    _ROUTE_COLOR = "#3498DB"

    def __init__(self, parent, dimensions):
        width, height = dimensions
        self._canvas = tk.Canvas(
            parent,
            width=width,
            height=height,
            highlightthickness=0)
        self._canvas.pack(fill=tk.BOTH, expand=True)

    def accept_dimensions(self, receiver) -> None:
        receiver.receive_dimensions(
            self._canvas.winfo_reqwidth(),
            self._canvas.winfo_reqheight())

    def clear(self) -> None:
        self._canvas.delete("all")

    def place(self, horizontal: float, vertical: float) -> None:
        self._canvas.create_oval(
            horizontal - self._CITY_RADIUS,
            vertical - self._CITY_RADIUS,
            horizontal + self._CITY_RADIUS,
            vertical + self._CITY_RADIUS,
            fill=self._CITY_COLOR,
            outline=self._CITY_COLOR)

    def connect(self, origin, destination) -> None:
        self._canvas.create_line(
            origin[0], origin[1],
            destination[0], destination[1],
            fill=self._ROUTE_COLOR,
            width=2)

    def schedule(self, delay: int, callback) -> str:
        return self._canvas.after(delay, callback)

    def cancel_schedule(self, schedule_identifier: str) -> None:
        self._canvas.after_cancel(schedule_identifier)