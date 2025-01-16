import random
import time
import unit


def battle(attack_units, defender_units):
    while len(attack_units) > 0 and len(defender_units) > 0:
        ranged_defenders = filter(lambda u: u.type == unit.UnitType.RANGED, defender_units)
        for i in ranged_defenders:
            target = random.choice(attack_units)
            i.attack(target)

        cavalry_attack = filter(lambda u: u.type == unit.UnitType.CAVALRY, attack_units)
        for i in cavalry_attack:
            target = sorted(defender_units, key=lambda x: x.melee_defense)[0]
            i.attack(target)

        cavalry_defenders = filter(lambda u: u.type == unit.UnitType.CAVALRY, defender_units)
        for i in cavalry_defenders:
            target = sorted(attack_units, key=lambda x: x.melee_defense).reverse()[0]
            i.attack(target)

        melee_attack = filter(lambda u: u.type == unit.UnitType.MELEE, attack_units)
        for i in melee_attack:
            target = random.choice(defender_units)
            i.attack(target)

        melee_defenders = filter(lambda u: u.type == unit.UnitType.MELEE, defender_units)
        for i in melee_defenders:
            target = random.choice(attack_units)
            i.attack(target)

        ranged_attack = filter(lambda u: u.type == unit.UnitType.RANGED, attack_units)
        for i in ranged_attack:
            target = random.choice(defender_units)
            i.attack(target)

        print("ATTACK UNITS:\n-------------")
        for i in attack_units:
            i.print_status()
        attack_units = list(filter(lambda x: x.number > 0 and x.morale > 0, attack_units))

        print("DEFENSE UNITS:\n-------------")
        for i in defender_units:
            i.print_status()
        defender_units = list(filter(lambda x: x.number > 0 and x.morale > 0, defender_units))

        input()


attack_units = [unit.FootSoldier(420)]
defender_units = [unit.FootSoldier(200), unit.Knight(75), unit.Archer(75)]

battle(attack_units, defender_units)