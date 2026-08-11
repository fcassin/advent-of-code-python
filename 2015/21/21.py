import collections
import functools
import itertools
import hashlib
from enum import Enum

from aoc import graph, ints, letter


def main():
    with open("input.txt", "r") as input_file:
        print(part1(input_file.readlines()))

    with open("input.txt", "r") as input_file:
        print(part2(input_file.readlines()))

class Character:
    def __init__(self, hit_points, damage, armor):
        self.hit_points = hit_points
        self.damage = damage
        self.armor = armor
    
    def equip(self, loadout):
        for equipment in loadout:
            self.damage += equipment.damage
            self.armor += equipment.armor
    
    def __str__(self):
        return f"Character(hit_points={self.hit_points}, damage={self.damage}, armor={self.armor})"

class EquipmentType(Enum):
    WEAPON = 1
    ARMOR = 2
    RING = 3
    
class Equipment:
    def __init__(self, name, cost, damage, armor, equipment_type):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.armor = armor
        self.equipment_type = equipment_type
        
    def __str__(self):
        return f"Equipment(name={self.name}, cost={self.cost}, damage={self.damage}, armor={self.armor}, equipment_type={self.equipment_type})"

weapons = [
    Equipment("Dagger", 8, 4, 0, EquipmentType.WEAPON),
    Equipment("Shortsword", 10, 5, 0, EquipmentType.WEAPON),
    Equipment("Warhammer", 25, 6, 0, EquipmentType.WEAPON),
    Equipment("Longsword", 40, 7, 0, EquipmentType.WEAPON),
    Equipment("Greataxe", 74, 8, 0, EquipmentType.WEAPON),
]

armors = [
    Equipment("Leather", 13, 0, 1, EquipmentType.ARMOR),
    Equipment("Chainmail", 31, 0, 2, EquipmentType.ARMOR),
    Equipment("Splintmail", 53, 0, 3, EquipmentType.ARMOR),
    Equipment("Bandedmail", 75, 0, 4, EquipmentType.ARMOR),
    Equipment("Platemail", 102, 0, 5, EquipmentType.ARMOR),
]

rings = [
    Equipment("Damage +1", 25, 1, 0, EquipmentType.RING),
    Equipment("Damage +2", 50, 2, 0, EquipmentType.RING),
    Equipment("Damage +3", 100, 3, 0, EquipmentType.RING),
    Equipment("Defense +1", 20, 0, 1, EquipmentType.RING),
    Equipment("Defense +2", 40, 0, 2, EquipmentType.RING),
    Equipment("Defense +3", 80, 0, 3, EquipmentType.RING),
]

def potential_loadouts():
    loadouts = set()
    for weapon in weapons:
        loadouts.add(tuple([weapon]))
        
    for weapon in weapons:
        for armor in armors:
            loadouts.add(tuple([weapon, armor]))
            
    for weapon in weapons:
        for ring1 in rings:
            loadouts.add(tuple([weapon, ring1]))
            for ring2 in rings:
                if ring1 != ring2:
                    loadouts.add(tuple([weapon, ring1, ring2]))
                    
    for weapon in weapons:
        for armor in armors:
            for ring1 in rings:
                loadouts.add(tuple([weapon, armor, ring1]))
                for ring2 in rings:
                    if ring1 != ring2:
                        loadouts.add(tuple([weapon, armor, ring1, ring2]))
                        
    return list(loadouts)

@functools.cache
def loadout_cost(loadout):
    total_cost = 0
    for equipment in loadout:
        total_cost += equipment.cost
    return total_cost

def fight(player, boss):
    attacker = player
    defender = boss
    
    while True:
        damage_dealt = max(1, attacker.damage - defender.armor)
        defender.hit_points -= damage_dealt
        
        if defender.hit_points <= 0:
            break
        
        attacker, defender = defender, attacker
        
    return defender == boss

def part1(input):
    hp = ints.extract(input[0])
    dmg = ints.extract(input[1])
    arm = ints.extract(input[2])
    
    for potential_loadout in sorted(potential_loadouts(), key=loadout_cost):
        player = Character(100, 0, 0)
        player.equip(potential_loadout)
        boss = Character(hp[0], dmg[0], arm[0])
        
        if fight(player, boss):
            return loadout_cost(potential_loadout)
        
    return 0

def part2(input):
    hp = ints.extract(input[0])
    dmg = ints.extract(input[1])
    arm = ints.extract(input[2])
    
    for potential_loadout in reversed(sorted(potential_loadouts(), key=loadout_cost)):
        player = Character(100, 0, 0)
        player.equip(potential_loadout)
        boss = Character(hp[0], dmg[0], arm[0])
        
        if not fight(player, boss):
            return loadout_cost(potential_loadout)
        
    return 0

if __name__ == "__main__":
    main()
