# Units
| Name         | Melee Attack | Melee Defense | Ranged Attack | Ranged Defense | Morale | Morale Impact | Wall Attack |
|--------------|--------------|---------------|---------------|----------------|--------|---------------|-------------|
| Brute        | 3            | 0             | 0             | 0              | 0.6    | 1.0           | 0           |
| Foot Soldier | 4            | 1             | 0             | 1              | 0.6    | 1.0           | 0           |
| Knight       | 6            | 2             | 0             | 4              | 0.6    | 1.0           | 0           |
| Archer       | 0            | 0             | 5             | 0              | 0.4    | 1.0           | 1           |
| Cavalry      | 4            | 0             | 0             | 0              | 0.4    | 2.5           | 0           |
| Catapult     | 0            | 0             | 10            | 0              | 0.1    | 1.0           | 20          |

### Combat Parameter Explanation
- **Unit Number** (represented in code as `number` and unlisted above) represents the number of that unit fighting. If it reaches 0, the unit is removed from battle (representing all units dying in battle).
- **Unit Morale** scales based on how many units there are, and as units take casualties they lose morale. It if reaches 0, the unit is removed from battle (representing all units retreating).
- **Melee Attack/Defense** determine how many casualties units take from melee attacks.
- **Ranged Attack/Defense** determine how many casualties units take from ranged attacks.
- **Morale Impact** determines how much enemy morale is impacted when they take casualties from the unit. For example, the **Cavalry**'s 2.5 morale impact means that for every casualty it deals, the enemy unit loses 2.5 morale.
- **Wall Attack** is unimplemented.

### Brute
Brutes are swarm units, with the worst attack of any melee unit. They're intended to have more morale than other units (0.6 per unit), but I accidentally set the Foot Soldier/Knight values to 0.6 too. **TODO: fix this. oops...**
Brutes' high morale means they can swarm enemies and take large casualties without retreating from battle.

### Foot Soldier & Knight
Foot Soldiers have better attack/defense than Brutes, and Knights have better attack/defense than Foot Soldiers.

### Archers
Archers are ranged units that can deal large amounts of damage to enemies, at the cost of no defense/low morale.

### Cavalry
Cavalry excel in destroying enemy morale, with an extremely high morale impact stat. They also attack much faster than melee/ranged units. While they can be powerful for forcing enemies to retreat by losing morale, their low morale and defense means they are not suited for long battles.

### Catapult
Catapults are siege weapons, used to destroy Walls (similar to Forts in HoI 4). Walls are unimplemented, though, so for now it is just another ranged unit.
