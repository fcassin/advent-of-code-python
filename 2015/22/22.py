import sys
sys.path.append("../../")

import collections
import functools
import graph
import ints
import itertools
import letter
import hashlib

from enum import Enum

def main():
    with open("input.txt", "r") as input_file:
        print(part1(input_file.readlines()))

    with open("input.txt", "r") as input_file:
        print(part2(input_file.readlines()))

class EffectType(Enum):
    SHIELD = 1
    POISON = 2
    RECHARGE = 3
    
class Effect:
    def __init__(self, effect_type, duration):
        self.effect_type = effect_type
        self.duration = duration
    
class Spell:
    def __init__(self, name, cost, damage, heal, effect_type=None, effect_duration=0):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.heal = heal
        self.effect_type = effect_type
        self.effect_duration = effect_duration
        
    def __str__(self):
        return f"Spell(name={self.name}, cost={self.cost}, damage={self.damage}, heal={self.heal}, effect_type={self.effect_type}, effect_duration={self.effect_duration})"

class Character:
    def __init__(self, hit_points, damage, mana):
        self.hit_points = hit_points
        self.damage = damage
        self.mana = mana
        self.armor = 0
        
    def __str__(self):
        return f"Character(hit_points={self.hit_points}, damage={self.damage}, mana={self.mana}, armor={self.armor})"
            
class State:
    def __init__(self, difficulty, player, boss, effects, mana_spent, turn, player_turn):
        self.difficulty = difficulty
        self.player = player
        self.boss = boss
        self.effects = effects  # List of Effect
        self.mana_spent = mana_spent
        self.turn = turn  # Current turn number
        self.player_turn = player_turn  # True if it's the player's turn, False if it's the boss's turn
        
    def apply_effects(self):
        self.player.armor = 0
        new_effects = []
        
        if self.difficulty == "hard" and self.player_turn:
            self.player.hit_points -= 1
        
        for effect in self.effects:
            if effect.effect_type == EffectType.SHIELD:
                self.player.armor = 7
            elif effect.effect_type == EffectType.POISON:
                self.boss.hit_points -= 3
            elif effect.effect_type == EffectType.RECHARGE:
                self.player.mana += 101
            
            effect.duration -= 1
            
            if effect.duration > 0:
                new_effects.append(effect)
        
        self.effects = new_effects
    
    def __str__(self):
        return f"State(player={self.player}, boss={self.boss}, effects={[str(e) for e in self.effects]}, mana_spent={self.mana_spent}, player_turn={self.player_turn})"

spells = [
    Spell("Magic Missile", 53, 4, 0),
    Spell("Drain", 73, 2, 2),
    Spell("Shield", 113, 0, 0, EffectType.SHIELD, 6),
    Spell("Poison", 173, 0, 0, EffectType.POISON, 6),
    Spell("Recharge", 229, 0, 0, EffectType.RECHARGE, 5),
]

def find_cheapest_win(initial_state):
    cheapest = float('inf')
    
    possible_states = collections.deque()
    possible_states.append(initial_state)
    
    while len(possible_states) > 0:
        state = possible_states.popleft()
    
        if state.mana_spent >= cheapest:
            continue 
        
        state.apply_effects()
        
        if state.player.hit_points <= 0:
            continue
        
        if state.boss.hit_points <= 0:
            cheapest = state.mana_spent
        
        if state.player_turn:
            for spell in spells:
                if spell.cost > state.player.mana:
                    continue
                
                if any(e.effect_type == spell.effect_type for e in state.effects):
                    continue
                
                new_player = Character(state.player.hit_points, state.player.damage, state.player.mana - spell.cost)
                new_boss = Character(state.boss.hit_points, state.boss.damage, state.boss.mana)
                
                new_effects = []
                for effect in state.effects:
                    new_effects.append(Effect(effect.effect_type, effect.duration))
                
                new_mana_spent = state.mana_spent + spell.cost
                new_player.hit_points += spell.heal
                new_boss.hit_points -= spell.damage
                
                if spell.effect_type is not None:
                    new_effects.append(Effect(spell.effect_type, spell.effect_duration))
                
                new_state = State(state.difficulty, new_player, new_boss, new_effects, new_mana_spent, state.turn + 1, False)
                possible_states.append(new_state)
        else:
            damage = max(1, state.boss.damage - state.player.armor)
            state.player.hit_points -= damage
            new_state = State(state.difficulty, state.player, state.boss, state.effects, state.mana_spent, state.turn + 1, True)
            possible_states.append(new_state)
            
    return cheapest

def part1(input):
    player = Character(hit_points=50, damage=0, mana=500)
    boss = Character(hit_points=58, damage=9, mana=0)
    
    initial_state = State("normal", player, boss, [], 0, 0, True)
        
    return find_cheapest_win(initial_state)

def part2(input):
    player = Character(hit_points=50, damage=0, mana=500)
    boss = Character(hit_points=58, damage=9, mana=0)
    
    initial_state = State("hard", player, boss, [], 0, 0, True)
        
    return find_cheapest_win(initial_state)

if __name__ == "__main__":
    main()