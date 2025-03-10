from enum import Enum
from random import uniform

class UnitType(Enum):
    MELEE = 1
    RANGED = 2
    CAVALRY = 3


class Unit:
    """Class storing data about units in the combat sim."""
    def __init__(self, t, n, ma, md, ra, rd, mo, mi, wa, name):
        self.type = t
        """Determines order of attack/whether unit uses ranged/melee attacks."""
        self.number = n
        """How many of this unit there are (ex. a Brute unit with number=500 represents 500 Brutes)."""
        self.max_number = n
        """Used to show how many units there were at the start of battle."""
        self.melee_attack = ma
        """How well this unit can use melee attacks."""
        self.melee_defense = md
        """How well this unit can defend against melee attacks."""
        self.ranged_attack = ra
        """How well this unit can use ranged attacks."""
        self.ranged_defense = rd
        """How well this unit can defend against ranged attacks."""
        self.morale = mo
        """Like Organization in HoI 4. If a unit loses all morale they retreat and cannot fight."""
        self.morale_impact = mi
        """How effective this unit is at destroying enemy morale."""
        self.wall_attack = wa
        """Unimplemented for now."""
        self.name = name
        """Unit's name."""
        self.kills = 0
        """Unused for the GUI version."""
        self.ui_element = None
        """Used to track UI elements for a unit, so they can be updated."""
        self.can_fight = True
        """Used to track if a unit can keep fighting."""

    def __str__(self):
        """Returns string representation of the unit."""
        return f"{self.name}x{self.number}"

    def attack(self, unit):
        """Logic for one unit to attack another."""
        if not self.can_fight or self.number <= 0 or self.morale <= 0:
            self.can_fight = False
            # ui_element may not be assigned if running headless mode, so it skips this step if there is no assigned UI element.
            if self.ui_element is not None:
                self.ui_element.show_out_of_battle()
            return

        casualties = 0
        if self.type == UnitType.RANGED:
            casualties = int((uniform(0, self.ranged_attack) - unit.ranged_defense) * (self.number / self.max_number) * (max(1.0, self.number / 100)))
        else:
            casualties = int((uniform(0, self.melee_attack) - unit.melee_defense) * (self.number / self.max_number)* (max(1.0, self.number / 100)))
        casualties = max(casualties, 0)
        unit.number -= casualties
        self.kills += casualties
        unit.number = max(unit.number, 0)
        unit.morale -= casualties * self.morale_impact
        
        if self.can_fight and unit.ui_element is not None:
            unit.ui_element.update_casualty_info(casualties, casualties * self.morale_impact)

class Brute(Unit):
    def __init__(self, n):
        super().__init__(UnitType.MELEE, n, 3, 0, 0, 0, int(0.6 * n), 1.0, 0, "Brutes")

class FootSoldier(Unit):
    def __init__(self, n):
        super().__init__(UnitType.MELEE, n, 4, 1, 0, 1, int(0.5 * n), 1.0, 0, "Foot Soldiers")

class Knight(Unit):
    def __init__(self, n):
        super().__init__(UnitType.MELEE, n, 6, 2, 0, 4, int(0.5 * n), 1.0, 0, "Knights")

class Archer(Unit):
    def __init__(self, n):
        super().__init__(UnitType.RANGED, n, 0, 0, 5, 0, int(0.4 * n), 1.0, 1, "Archers")

class Cavalry(Unit):
    def __init__(self, n):
        super().__init__(UnitType.CAVALRY, n, 4, 0, 0, 0, int(0.4 * n), 2.5, 0, "Cavalry")

class Catapult(Unit):
    def __init__(self, n):
        super().__init__(UnitType.RANGED, n, 0, 0, 10, 0, int(0.1 * n), 1.0, 20, "Catapults")