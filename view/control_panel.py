import tkinter as tk

class ControlPanel:
    _DEFAULT_CITY_COUNT = 10

    def __init__(self, parent, factory):
        frame = factory.create_frame(parent)
        factory.create_label(frame, "Cities:")
        self._city_spinner = self._configure(factory, frame)
        self._start_button = factory.create_button(frame, "Start")
        self._stop_button = factory.create_button(frame, "Stop")
        self._stop_button.config(state=tk.DISABLED)
        self._reset_button = factory.create_button(frame, "Reset")
        self._reset_button.config(state=tk.DISABLED)

    def register(self, listener) -> None:
        self._start_button.config(command=listener.on_start_requested)
        self._stop_button.config(command=listener.on_stop_requested)
        self._reset_button.config(command=listener.on_reset_requested)

    def accept_count(self, receiver) -> None:
        receiver.receive_count(self._city_spinner.get())

    def enable_start(self) -> None:
        self._start_button.config(state=tk.NORMAL)
        self._stop_button.config(state=tk.DISABLED)
        self._reset_button.config(state=tk.NORMAL)

    def complete(self) -> None:
        self._start_button.config(state=tk.DISABLED)
        self._stop_button.config(state=tk.DISABLED)
        self._reset_button.config(state=tk.NORMAL)

    def disable_reset(self) -> None:
        self._reset_button.config(state=tk.DISABLED)

    def enable_stop(self) -> None:
        self._start_button.config(state=tk.DISABLED)
        self._stop_button.config(state=tk.NORMAL)

    def _configure(self, factory, frame):
        spinner = factory.create_spinner(frame, (5, 50))
        spinner.delete(0, tk.END)
        spinner.insert(0, str(self._DEFAULT_CITY_COUNT))
        return spinner