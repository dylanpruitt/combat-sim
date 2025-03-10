from enum import Enum
from tkinter import StringVar, Tk, ttk

from battle_logic import battle_step, simulate_battle
from combat_unit import CombatUnitUI
from staged_unit import StagedUnitUI
from time_control_ui import TimeControlUI
import unit
from unit_adder_ui import UnitAdderUI


class UIStates(Enum):
    UNIT_INPUT = 0,
    COMBAT = 1,
    RESULTS = 2,

class MainUI(ttk.Frame):
    """Main UI class."""
    def __init__(self, parent):
        super().__init__(parent)

        # Initialize class fields
        self.attack_units = [unit.Brute(600), unit.Archer(250)]
        self.defense_units = [unit.Brute(200), unit.Cavalry(100), unit.FootSoldier(100)]
        self.speed = 1.0
        self.interrupt = True
        self.battle_turn = 1
        self.ui_state = None

        # Status bar (shows if combat is paused/running)
        self.state_frame = ttk.Frame(self)
        self.state_frame.grid(column=0, row=0, sticky="ew")
        self.state_frame.grid_columnconfigure(0, weight=1)
        self.state_str = StringVar(value="Paused")
        self.state_text = ttk.Label(self.state_frame, textvariable=self.state_str, background="#666",
            foreground="#fff", anchor="center")
        self.state_text.grid(column=0, row=0, sticky="ew")

        # Displays attacker/defender units.
        self.unit_frame = ttk.Frame(self)
        self.unit_frame.grid(column=0, row=1, sticky="nsew")
        self.unit_frame.grid_columnconfigure(0, weight=1)
        self.unit_frame.grid_columnconfigure(1, weight=1)

        self.atk_frame = ttk.Frame(self.unit_frame)
        self.atk_frame.grid(column=0, row=0, sticky="n")
        self.atk_frame.grid_columnconfigure(0, weight=1)
        self.def_frame = ttk.Frame(self.unit_frame)
        self.def_frame.grid(column=1, row=0, sticky="n")
        self.def_frame.grid_columnconfigure(0, weight=1)
        ttk.Label(self.atk_frame, text="Attacker Units", name="unit_atk", anchor="w").grid(column=0, sticky="ew")
        ttk.Label(self.def_frame, text="Defender Units", name="unit_def", anchor="w").grid(column=0, sticky="ew")

        self.control_str = StringVar(value="")
        self.control_text = ttk.Label(self, textvariable=self.control_str, anchor="center")
        self.control_text.grid(row=4, sticky="ew")

        self.bottom_widget = None
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.set_ui_mode(UIStates.UNIT_INPUT)

    def set_unit_adder_as_bottom_widget(self):
        """Sets UnitAdderUI as the bottom widget."""
        if self.bottom_widget is not None:
            self.bottom_widget.destroy()
        self.bottom_widget = UnitAdderUI(self)
        self.bottom_widget.borderwidth = 2
        self.bottom_widget.relief = "flat"
        self.bottom_widget.grid(column=0, row=2, sticky="nsew", padx=8, pady=(0,8))

    def set_time_control_as_bottom_widget(self):
        """Sets TimeControlUI as the bottom widget."""
        if self.bottom_widget is not None:
            self.bottom_widget.destroy()
        self.bottom_widget = TimeControlUI(self)
        self.bottom_widget.grid(column=0, row=2, sticky="nsew", padx=8, pady=(0,8))
    
    def populate_staged_units(self):
        """Populates unit staging UI using unit listing."""
        for w in self.atk_frame.winfo_children():
            if "unit" not in str(w):
                w.destroy()
        for w in self.def_frame.winfo_children():
            if "unit" not in str(w):
                w.destroy()
        for u in self.attack_units:
            StagedUnitUI(self.atk_frame, u, self.attack_units)
        for u in self.defense_units:
            StagedUnitUI(self.def_frame, u, self.defense_units)

    def populate_combat_units(self):
        """Populates unit combat UI using unit listing."""
        for w in self.atk_frame.winfo_children():
            if "unit" not in str(w):
                w.destroy()
        for w in self.def_frame.winfo_children():
            if "unit" not in str(w):
                w.destroy()
        for u in self.attack_units:
            CombatUnitUI(self.atk_frame, u)
        for u in self.defense_units:
            CombatUnitUI(self.def_frame, u)

    def set_ui_mode(self, new_mode:UIStates):
        """Handles logic for what each UI mode should look like."""
        match new_mode:
            case UIStates.COMBAT:
                self.ui_state = UIStates.COMBAT
                self.populate_combat_units()
                self.set_time_control_as_bottom_widget()
                self.control_str.set("Controls: [Space]: pause/resume battle [L/R Arrows]: change simulation speed [Enter]: switch to unit input")
                self.state_str.set("Paused")
            case UIStates.UNIT_INPUT:
                # Kind of a lazy way to work around unit objects not changing after battle sim, but it works.
                self.attack_units = [unit.Brute(600), unit.Archer(250)]
                self.defense_units = [unit.Brute(200), unit.Cavalry(100), unit.FootSoldier(100)]
                self.populate_staged_units()
                self.set_unit_adder_as_bottom_widget()
                self.control_str.set("Controls: [R]: run headless simulation (shows attacker win rate with matchup) [Enter]: switch to unit input")
                self.state_str.set("Selecting units")
        self.ui_state = new_mode
    

    def switch(self):
        """Used to test switching between UI modes."""
        if self.ui_state != UIStates.UNIT_INPUT:
            self.set_ui_mode(UIStates.UNIT_INPUT)
        else:
            self.set_ui_mode(UIStates.COMBAT)

    def start_combat(self):
        """Starts running the combat sim."""
        self.interrupt = False
        self.state_str.set("Running")
        self.state_text.config(background="#66a")
        self.combat_step()

    def combat_step(self):
        """Logic handling one turn of combat. It will keep calling itself until the combat is stopped."""
        if self.interrupt:
            self.stop_combat()
            return

        still_fighting = battle_step(self.attack_units, self.defense_units)
        if still_fighting:
            self.after(int(1000 / self.speed), self.combat_step)
        else:
            self.stop_combat()
            attacker_casualties = 0
            for u in self.attack_units:
                attacker_casualties += u.max_number - u.number
            defender_casualties = 0
            for u in self.defense_units:
                defender_casualties += u.max_number - u.number
            self.state_str.set(f"Battle over. Attackers lost {attacker_casualties} units; defenders lost {defender_casualties}.")

    def stop_combat(self):
        """Pauses the combat sim."""
        self.interrupt = True
        self.state_str.set("Paused")
        self.state_text.config(background="#666")

    def handle_input(self, key_event):
        """Handles keyboard input."""
        keysym = key_event.keysym

        if self.ui_state == UIStates.COMBAT:
            if keysym == "Left":
                self.bottom_widget.mod_speed(0.5)
            if keysym == "Right":
                self.bottom_widget.mod_speed(2.0)
            if keysym == "space":
                if self.interrupt:
                    self.start_combat()
                else:
                    self.stop_combat()
        else:
            if keysym == "q":
                # test code to check unit amount/names properly show when adding
                print([str(x) for x in self.attack_units])
                print([str(x) for x in self.defense_units])
            if keysym == "r":
                # run headless simulation to see matchup win stats
                self.state_str.set(f"Running simulated matchup...")
                NUM_BATTLES = 1000
                count_won_attacker = 0
                for i in range(NUM_BATTLES):
                    count_won_attacker += int(simulate_battle(self.attack_units, self.defense_units))
                attacker_win_rate = round(count_won_attacker * 100 / NUM_BATTLES, 2)
                self.state_str.set(f"Out of {NUM_BATTLES} battles, attackers would win {count_won_attacker} ({attacker_win_rate}%)")

    def back(self):
        """Handles the user going back to the unit select screen."""
        if self.ui_state == UIStates.COMBAT:
            self.set_ui_mode(UIStates.UNIT_INPUT)

def main():
    root = Tk()
    root.title("Combat Sim")
    root.minsize(640, 360)
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)
    main_ui = MainUI(root)
    main_ui.grid(padx=8, pady=8, sticky="nsew")
    root.bind('<Key>', main_ui.handle_input)
    root.bind("<Escape>", lambda _: main_ui.back())
    root.bind("<Return>", lambda _: main_ui.switch())

    root.mainloop()

if __name__ == "__main__":
    main()