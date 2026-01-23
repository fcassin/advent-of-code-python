import sys
sys.path.append("../../")

import collections
import functools
import graph
import grid
import hashlib
import ints
import itertools
import letter
import math
import png
import screen
import z3

def main():
    with open("input.txt", "r") as input_file:
        print(part1(input_file.readlines()))

    with open("input.txt", "r") as input_file:
        print(part2(input_file.readlines()))
    
class Machine:
    def __init__(self, diagram, buttons, joltage):
        self.diagram = diagram
        self.buttons = buttons
        self.joltage = joltage
        
    def __str__(self):
        return f"Machine(diagram={self.diagram}, buttons={self.buttons}, joltage={self.joltage})"
    
def light(machine):
    # print(f"Lighting machine with diagram {machine.diagram}, buttons {machine.buttons}, joltage {machine.joltage}")    
    states = collections.deque()
    
    state = list('.' * len(machine.diagram))
    states.append((0, state)) # button presses, diagram state
    
    SEEN = set()
    while len(states) > 0:
        presses, state = states.popleft()
        
        if "".join(state) == machine.diagram:
            return presses
        
        if "".join(state) in SEEN:
            continue
        SEEN.add("".join(state))
        
        for button_configuration in machine.buttons:
            new_state = state[:]
                        
            for button in button_configuration:
                if new_state[button] == '#':
                    new_state[button] = '.'
                else:
                    new_state[button] = '#'
            
            states.append((presses + 1, new_state))
            
def z3jolt_explicit():
    buttonA = z3.Int('buttonA') # 3
    buttonB = z3.Int('buttonB') # 1,3
    buttonC = z3.Int('buttonC') # 2
    buttonD = z3.Int('buttonD') # 2,3
    buttonE = z3.Int('buttonE') # 0,2
    buttonF = z3.Int('buttonF') # 0,1
    
    optimizer = z3.Optimize()
    optimizer.add(buttonA >= 0)
    optimizer.add(buttonB >= 0)
    optimizer.add(buttonC >= 0)
    optimizer.add(buttonD >= 0)
    optimizer.add(buttonE >= 0)
    optimizer.add(buttonF >= 0)
    
    # 3, 5, 4, 7
    optimizer.add((sum([buttonE, buttonF]) == 3)) # position 0
    optimizer.add((sum([buttonB, buttonF]) == 5)) # position 1
    optimizer.add((sum([buttonC, buttonD, buttonE]) == 4)) # position 2
    optimizer.add((sum([buttonA, buttonB, buttonD]) == 7)) # position 4
    
    total_presses = z3.Int('total_presses')
    optimizer.add(total_presses == buttonA + buttonB + buttonC + buttonD + buttonE + buttonF)
    
    optimizer.minimize(total_presses)
    if optimizer.check() == z3.sat:
        model = optimizer.model()
        return model[total_presses].as_long()
    else:
        return -1
    
def z3jolt(machine):
    optimizer = z3.Optimize()
    
    buttons = []
    for index, button_configuration in enumerate(machine.buttons):
        button = z3.Int(f'button_{index}')
        optimizer.add(button >= 0)
        buttons.append(button)
        
    for index, value in enumerate(machine.joltage):
        involved_in_joltage = []
        
        for button_index, button_configuration in enumerate(machine.buttons):
            if index in button_configuration:
                button = buttons[button_index]
                involved_in_joltage.append(button)
        
        optimizer.add(z3.Sum(involved_in_joltage) == value)
        
    total_presses = z3.Int('total_presses')
    optimizer.add(total_presses == sum(buttons))
    optimizer.minimize(total_presses)
    
    if optimizer.check() == z3.sat: # sat stands for satisfiable
        model = optimizer.model()
        return model[total_presses].as_long()
    else:
        assert False, "Unsatisfiable Z3 constraints"
    
MACHINES = []    
    
def part1(input):
    total = 0
    global MACHINES
    
    for line in input:
        line = line.strip()
        
        split = line.split(' ')
        diagram = split.pop(0).replace('[', '').replace(']', '')
        joltage = ints.extract(split.pop())
        
        buttons = []
        for button in split:
            buttons.append(ints.extract(button))
        
        machine = Machine(diagram, buttons, joltage)
        # print(machine)
        MACHINES.append(machine)
        
        total = total + light(machine)
        
    return total

def part2(input):
    _ = input
    total = 0 
    
    for machine in MACHINES:
        total = total + z3jolt(machine) 
        
    return total

if __name__ == "__main__":
    main()