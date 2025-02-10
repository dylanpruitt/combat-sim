from tkinter import StringVar, ttk

MIN_SPEED = 0.125
MAX_SPEED = 8

class TimeControlUI(ttk.Frame):
    """Class for UI allowing users to change combat speed."""
    def __init__(self, parent):
        super().__init__(parent)
        self.anchor = "center"
        self.parent = parent
        self.speed_string = StringVar(value=str(self.parent.speed))
        self.speed_label = ttk.Label(self, width=6, textvariable=self.speed_string, anchor="center")
        self.speed_label.grid(column=1, row=0)
        self.slow_button = ttk.Button(self, text="<", width=1, command=lambda: self.mod_speed(0.5))
        self.slow_button.grid(column=0, row=0, sticky="e")
        self.fast_button = ttk.Button(self, text=">", width=1, command=lambda: self.mod_speed(2.0))
        self.fast_button.grid(column=2, row=0, sticky="w")
        # Centers the buttons/label horizontally.
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)


    def mod_speed(self, mod):
        """Changes combat speed."""
        if (self.parent.speed == MIN_SPEED and mod < 1) \
            or (self.parent.speed == MAX_SPEED and mod > 1):
            return
        self.parent.speed *= mod
        self.speed_string.set(str(self.parent.speed))

        # Disables slow/fast buttons if combat speed is set to min/max value.
        if self.parent.speed == MIN_SPEED:
            self.slow_button.state(["disabled"])
        else:
            self.slow_button.state(["!disabled"])
        if self.parent.speed == MAX_SPEED:
            self.fast_button.state(["disabled"])
        else:
            self.fast_button.state(["!disabled"])