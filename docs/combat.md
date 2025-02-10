# Combat
Combat is turn-based; each turn, units attack in steps (see below) so that different units act faster than others. At the end of each turn, if a unit has nobody left alive (`number <= 0`) or no morale (`morale <= 0`), it will be considered unable to fight and removed from battle.

### Attack Order  
1 - Defender Ranged Units  
2 - Attacker Cavalry Units  
3 - Defender Cavalry Units  
4 - Attacker Melee Units  
5 - Defender Melee Units  
6 - Attacker Ranged Units  

### Attacking
When it's a unit's turn to attack, it calls the `Unit.attack` found in unit.py.  
If the unit cannot fight, it is unable to attack and does nothing. Otherwise, the unit inflicts casualties on the enemy unit based on the formula below (slightly simplified from the code):  
`casualties = random(0, self.attack) - enemy.defense) * alive_unit_ratio * unit_num_modifier`

Although a unit can have high attack and still cause 0 casualties, enemy defense is ALWAYS subtracted from the base figure. This casualty figure is multiplied by the percent of alive units still left from the start of battle (`alive_unit_ratio`) and a modifier giving units with larger numbers higher damage (`unit_num_modifier`). `unit_num_modifier` gives units with `number > 100` a boost in combat, but does not penalize units with `number < 100`.  
The enemy unit then loses casualties based on the figure above, and loses morale for each casualty inflicted. Because units get weaker as they take damage, units that attack early in a turn (ranged defense/cavalry attack) can get an advantage by wearing down slower units before they get a chance to act.

[Back to README.md](../README.md)
