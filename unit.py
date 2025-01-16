from enum import Enum
from random import uniform, randint

class UnitType(Enum):
    MELEE = 1
    RANGED = 2
    CAVALRY = 3


class Unit:
    def __init__(self, t, n, ma, md, ra, rd, mo, mi, wa, name):
        self.type = t
        self.number = n
        self.max_number = n
        self.melee_attack = ma
        self.melee_defense = md
        self.ranged_attack = ra
        self.ranged_defense = rd
        self.morale = mo
        self.morale_impact = mi
        self.wall_attack = wa
        self.name = name
        self.kills = 0

    def attack(self, unit):
        if self.number <= 0 or self.morale <= 0:
            print(f"{self.name} cannot fight")
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
        print(f"{self.name} attack {unit.name} (-{casualties} units/-{casualties * self.morale_impact} morale)")

    def print_status(self):
        print(f"{self.name}: {self.number}/{self.max_number} UNITS, {self.morale} MORALE, {self.kills} KILLS")

class Brute(Unit):
    def __init__(self, n):
        super().__init__(UnitType.MELEE, n, 3, 0, 0, 0, 0.6 * n, 1.0, 0, "Brutes")

class FootSoldier(Unit):
    def __init__(self, n):
        super().__init__(UnitType.MELEE, n, 4, 1, 0, 1, 0.6 * n, 1.0, 0, "Foot Soldiers")

class Knight(Unit):
    def __init__(self, n):
        super().__init__(UnitType.MELEE, n, 6, 2, 0, 4, 0.6 * n, 1.0, 0, "Knights")

class Archer(Unit):
    def __init__(self, n):
        super().__init__(UnitType.RANGED, n, 0, 0, 5, 0, 0.4 * n, 1.0, 1, "Archers")

class Cavalry(Unit):
    def __init__(self, n):
        super().__init__(UnitType.CAVALRY, n, 4, 0, 0, 0, 0.4 * n, 2.5, 0, "Cavalry")

class Catapult(Unit):
    def __init__(self, n):
        super().__init__(UnitType.RANGED, n, 0, 0, 10, 0, 0.1 * n, 1.0, 20, "Catapults")