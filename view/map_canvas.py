import tkinter as tk

class MapCanvas:
    _CITY_RADIUS = 6
    _CITY_COLOR = "#E74C3C"
    _ROUTE_COLOR = "#3498DB"
    _BACKGROUND = "#1A252F"

    def __init__(self, parent, dimensions):
        width, height = dimensions
        border = tk.Frame(
            parent,
            bg=self._BACKGROUND,
            highlightbackground="#455A64",
            highlightthickness=1)
        border.pack(fill=tk.BOTH, expand=True, padx=12, pady=(4, 12))
        self._canvas = tk.Canvas(
            border,
            width=width,
            height=height,
            bg=self._BACKGROUND,
            highlightthickness=0)
        self._canvas.pack(fill=tk.BOTH, expand=True)

    def accept_dimensions(self, receiver) -> None:
        receiver.receive_dimensions(
            self._canvas.winfo_reqwidth(),
            self._canvas.winfo_reqheight())

    def clear(self) -> None:
        self._canvas.delete("all")

    def place(self, horizontal, vertical) -> None:
        self._canvas.create_oval(
            horizontal - self._CITY_RADIUS,
            vertical - self._CITY_RADIUS,
            horizontal + self._CITY_RADIUS,
            vertical + self._CITY_RADIUS,
            fill=self._CITY_COLOR,
            outline="#C0392B",
            width=2)

    def connect(self, origin, destination) -> None:
        self._canvas.create_line(
            origin[0], origin[1],
            destination[0], destination[1],
            fill=self._ROUTE_COLOR,
            width=2)

    def schedule(self, delay, callback) -> str:
        return self._canvas.after(delay, callback)

    def cancel_schedule(self, schedule_identifier) -> None:
        self._canvas.after_cancel(schedule_identifier)