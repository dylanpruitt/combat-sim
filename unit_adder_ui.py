from tkinter import *
from tkinter import ttk
from staged_unit import StagedUnitUI
from unit import *

class UnitAdderUI(ttk.Frame):
    """Class for UI allowing users to add a unit to the combat sim."""
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.name_label = ttk.Label(self, text="Add ")
        self.name_label.grid(column=0,row=0, sticky="se")
        # Entry for players to change unit amount
        self.amount_str = StringVar(value="10")
        self.check_wrapper = (parent.register(check_numeric), '%P')
        self.amount_entry = ttk.Entry(self, width=4, textvariable=self.amount_str, validate='all', validatecommand=self.check_wrapper)
        self.amount_entry.grid(column=1,row=0, sticky="se")

        self.name_label2 = ttk.Label(self, text=" of ")
        self.name_label2.grid(column=2,row=0, sticky="s")

        # Combobox for players to select unit type to add
        self.unit_name = StringVar(value='Brute')
        self.unitbox = ttk.Combobox(self,
            values=['Brute', 'Foot Soldier', 'Knight', 'Cavalry', 'Archer'],
            textvariable=self.unit_name, state="readonly")
        self.unitbox.grid(column=3,row=0, sticky="s")
        self.unitbox.bind("<<ComboboxSelected>>", lambda _: self.unitbox.selection_clear())
        self.add_button = ttk.Button(self, text="Add", command=self.add_unit)
        self.add_button.grid(column=4, row=0, sticky="s")

        self.team_label = ttk.Label(self, text=" to ")
        self.team_label.grid(column=5, row=0, sticky="s")

        # Combobox for players to choose which side (attack/defense) to add units to
        self.team_name = StringVar(value='attackers')
        self.teambox = ttk.Combobox(self, values=['attackers', 'defenders'], width=9,
            textvariable=self.team_name, state="readonly")
        self.teambox.grid(column=6, row=0, sticky="sw")
        # Centers this UI horizontally.
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(6, weight=1)
        self.grid_rowconfigure(0, weight=1)


    def add_unit(self):
        """Adds a unit to the unit listing."""
        if self.unitbox.get() == "":
            return

        unit_amount = int(self.amount_str.get())
        unit = None

        match self.unit_name.get():
            case "Brute":
                unit = Brute(unit_amount)
            case "Foot Soldier":
                unit = FootSoldier(unit_amount)
            case "Knight":
                unit = Knight(unit_amount)
            case "Cavalry":
                unit = Cavalry(unit_amount)
            case "Archer":
                unit = Archer(unit_amount)

        selected_team = self.parent.attack_units
        selected_team_frame = self.parent.atk_frame
        if self.team_name.get() == "defenders":
            selected_team = self.parent.defense_units
            selected_team_frame = self.parent.def_frame

        StagedUnitUI(selected_team_frame, unit, selected_team)
        selected_team.append(unit)

def check_numeric(newval):
    try:
        amt = int(newval)
        return amt > 0
    except ValueError:
        return False