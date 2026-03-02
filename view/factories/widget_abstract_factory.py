import tkinter as tk

class WidgetAbstractFactory:
    _PADDING = 5
    _FONT = ("Helvetica", 12)
    _FOREGROUND = "#ECF0F1"
    _BACKGROUND = "#34495E"

    def create_label(self, parent, text):
        widget = tk.Label(
            parent, text=text,
            font=self._FONT,
            fg=self._FOREGROUND,
            bg=self._BACKGROUND)
        widget.pack(side=tk.LEFT, padx=self._PADDING, pady=self._PADDING)
        return widget

    def create_button(self, parent, text):
        widget = tk.Button(parent, text=text, width=8)
        widget.pack(side=tk.LEFT, padx=self._PADDING)
        return widget

    def create_spinner(self, parent, bounds):
        minimum, maximum = bounds
        widget = tk.Spinbox(
            parent, from_=minimum, to=maximum,
            width=4, font=self._FONT)
        widget.pack(side=tk.LEFT, padx=self._PADDING)
        return widget

    def create_frame(self, parent):
        widget = tk.Frame(parent, bg=self._BACKGROUND)
        widget.pack(side=tk.TOP, fill=tk.X, pady=self._PADDING)
        return widget