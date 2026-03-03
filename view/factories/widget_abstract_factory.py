import tkinter as tk
from tkinter import ttk

class WidgetAbstractFactory:
    _TOOLBAR_PADDING = 8
    _ELEMENT_SPACING = 6
    _FONT_BODY = ("Helvetica", 11)
    _FONT_STATISTICS = ("Helvetica", 13, "bold")
    _FOREGROUND = "#ECF0F1"
    _BACKGROUND = "#34495E"
    _BUTTON_STYLES = {
        "Start": "Start.TButton",
        "Stop": "Stop.TButton",
        "Reset": "Reset.TButton"
    }

    def __init__(self, root):
        self._style = ttk.Style(root)
        self._style.theme_use("clam")
        self._configure_buttons()
        self._configure_spinner()

    def _configure_buttons(self):
        self._define_variant("Start.TButton", ("#27AE60", "#2ECC71"))
        self._define_variant("Stop.TButton", ("#C0392B", "#E74C3C"))
        self._define_variant("Reset.TButton", ("#7F8C8D", "#95A5A6"))

    def _define_variant(self, name, colors):
        background, hover = colors
        self._style.configure(
            name,
            font=("Helvetica", 10, "bold"),
            foreground="#FFFFFF",
            background=background,
            borderwidth=0,
            padding=(14, 6),
            focuscolor=background)
        self._style.map(
            name,
            background=[("active", hover), ("disabled", "#4A5568")],
            foreground=[("disabled", "#718096")])

    def _configure_spinner(self):
        self._style.configure(
            "Dark.TSpinbox",
            fieldbackground="#2C3E50",
            foreground=self._FOREGROUND,
            background=self._BACKGROUND,
            arrowcolor=self._FOREGROUND,
            borderwidth=1,
            padding=4)

    def create_label(self, parent, text):
        widget = tk.Label(
            parent, text=text,
            font=self._FONT_BODY,
            fg=self._FOREGROUND,
            bg=self._BACKGROUND)
        widget.pack(
            side=tk.LEFT,
            padx=self._ELEMENT_SPACING,
            pady=self._TOOLBAR_PADDING)
        return widget

    def create_statistics_label(self, parent, text):
        widget = tk.Label(
            parent, text=text,
            font=self._FONT_STATISTICS,
            fg=self._FOREGROUND,
            bg=self._BACKGROUND,
            anchor=tk.CENTER)
        widget.pack(
            side=tk.LEFT,
            expand=True,
            padx=self._ELEMENT_SPACING)
        return widget

    def create_button(self, parent, text):
        style_name = self._BUTTON_STYLES.get(text, "TButton")
        widget = ttk.Button(
            parent, text=text,
            style=style_name, width=8)
        widget.pack(side=tk.LEFT, padx=self._ELEMENT_SPACING)
        return widget

    def create_spinner(self, parent, bounds):
        minimum, maximum = bounds
        widget = ttk.Spinbox(
            parent, from_=minimum, to=maximum,
            width=4, font=self._FONT_BODY,
            style="Dark.TSpinbox")
        widget.pack(side=tk.LEFT, padx=self._ELEMENT_SPACING)
        return widget

    def create_frame(self, parent):
        widget = tk.Frame(parent, bg=self._BACKGROUND)
        widget.pack(
            side=tk.TOP, fill=tk.X,
            pady=(self._TOOLBAR_PADDING, 0),
            padx=self._TOOLBAR_PADDING)
        return widget
