from tkinter import font, StringVar, ttk

class CombatUnitUI():
    """Class for UI showing detailed combat information about units."""
    def __init__(self, parent, unit):
        row = parent.grid_size()[1]
        self.unit = unit
        self.unit.ui_element = self
        self.status = StringVar(value="IN BATTLE")
        # Shows name/status
        self.high_level = ttk.Frame(parent)
        self.high_level.grid(column=0, row=row, sticky="nsw")
        self.name_label = ttk.Label(self.high_level, text=self.unit.name)
        self.name_label.grid(column=0, row=0, sticky="w")
        self.status_label = ttk.Label(self.high_level, textvariable=self.status)
        self.status_label.grid(column=0, row=1)
        # Shows detailed stat breakdown
        self.low_level = ttk.Frame(parent)
        self.low_level.grid(column=1,row=row, sticky="nse")
        self.ul = ttk.Label(self.low_level, text="Units")
        self.ul.grid(column=0, row=0, sticky="w")
        self.ml = ttk.Label(self.low_level, text="Morale")
        self.ml.grid(column=0, row=1, sticky="w")
        # Amount/Morale labels
        bold_font = font.Font(size=10, weight="bold")
        self.amt_str = StringVar(value=f"{self.unit.number}/{self.unit.max_number}")
        self.amt_label = ttk.Label(self.low_level, textvariable=self.amt_str, font=bold_font)
        self.amt_label.grid(column=1, row=0, sticky="e")
        self.damt_str = StringVar(value="(-0)")
        self.damt_label = ttk.Label(self.low_level, textvariable=self.damt_str)
        self.damt_label.grid(column=2, row=0, sticky="e")

        self.mo_str = StringVar(value=f"{self.unit.morale}")
        self.mo_label = ttk.Label(self.low_level, textvariable=self.mo_str, font=bold_font)
        self.mo_label.grid(column=1, row=1, sticky="e")
        self.dmo_str = StringVar(value="(-0)")
        self.dmo_label = ttk.Label(self.low_level, textvariable=self.dmo_str)
        self.dmo_label.grid(column=2, row=1, sticky="e")

    def show_out_of_battle(self):
        """Grays out UI text for units that cannot fight."""
        if self.unit.number <= 0:
            self.status.set("ANNIHILATED")
        else:
            self.status.set("RETREATED")
        
        self.name_label.config(foreground="#444")
        self.status_label.config(foreground="#444")
        self.amt_label.config(foreground="#444")
        self.damt_label.config(foreground="#444")
        self.mo_label.config(foreground="#444")
        self.dmo_label.config(foreground="#444")
        self.ul.config(foreground="#444")
        self.ml.config(foreground="#444")

    def update_casualty_info(self, casualties, morale_loss):
        """Updates UI with new casualties/morale loss."""
        self.amt_str.set(f"{self.unit.number}/{self.unit.max_number}")
        self.mo_str.set(f"{self.unit.morale}")
        self.damt_str.set(f"(-{casualties})")
        self.dmo_str.set(f"(-{morale_loss})")

        if casualties > 0:
            self.damt_label.config(foreground="#f00")
        else:
            self.damt_label.config(foreground="#444")
        if morale_loss > 0:
            self.dmo_label.config(foreground="#f00")
        else:
            self.dmo_label.config(foreground="#444")