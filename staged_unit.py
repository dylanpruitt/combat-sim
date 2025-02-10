from tkinter import StringVar, ttk
from unit import Unit

class StagedUnitUI:
    """Class for UI displaying info about units before the combat sim starts."""
    def __init__(self, parent, unit_data:Unit, unit_list):
        row = parent.grid_size()[1]
        self.name = unit_data.name
        self.parent = parent
        self.unit_data = unit_data
        self.unit_list = unit_list
        self.name_label = ttk.Label(parent, text=unit_data.name)
        self.name_label.grid(column=0, row=row, sticky="w")
        # Users can edit the amount of a unit with this UI after adding units.
        self.amount_str = StringVar(value=unit_data.number)
        self.amount_str.trace_add("write", self.update_amount)
        self.check_wrapper = (parent.register(check_numeric), '%P')
        self.amount_entry = ttk.Entry(parent, width=4, textvariable=self.amount_str, validate='all', validatecommand=self.check_wrapper)
        self.amount_entry.grid(column=1, row=row, sticky="e")
        self.remove_button = ttk.Button(parent, text="X", width=1, command=self.remove)
        self.remove_button.grid(column=2, row=row, sticky="e", padx=8)

    def update_amount(self, *args):
        """Updates the unit listing with new amount."""
        self.unit_data.__init__(int(self.amount_str.get()))

    def remove(self):
        """Removes unit from the unit listing."""
        self.unit_list.remove(self.unit_data)
        self.name_label.destroy()
        self.amount_entry.destroy()
        self.remove_button.destroy()
        


def check_numeric(newval):
    try:
        amt = int(newval)
        return amt > 0
    except ValueError:
        return False