import copy
import random
import unit

def simulate_battle(au, du):
    """Quickly simulates a battle without showing anything in the UI."""
    au_copy = copy.deepcopy(au)
    du_copy = copy.deepcopy(du)

    while len([u for u in au_copy if u.can_fight]) > 0 and len([u for u in du_copy if u.can_fight]) > 0:
        battle_step(au_copy, du_copy)
    # returns true if attackers are left (they won), false if attackers died (defenders won)
    return len([u for u in au_copy if u.can_fight]) > 0

def battle_step(au, du):
    """Logic representing one turn in the combat sim. Units fight in a predetermined order."""
    attack_units = [u for u in au if u.can_fight]
    defender_units = [u for u in du if u.can_fight]

    if len(attack_units) > 0 and len(defender_units) > 0:
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
            target = sorted(attack_units, key=lambda x: x.melee_defense)[0]
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
        return True
    else:
        return False