import sys
sys.path.append("../../")

import collections
import functools
import graph
import grid
import ints
import itertools
import letter
import hashlib
import screen

def main():
    with open("input.txt", "r") as input_file:
        print(part1(input_file.readlines()))

    with open("input.txt", "r") as input_file:
        print(part2(input_file.readlines()))
    
REGISTERS = {
    'a': 0,
    'b': 0,
    'c': 0,
    'd': 0,
}

CURRENT_INSTRUCTION = 0 
    
def copy(x, y):
    global CURRENT_INSTRUCTION
    if x in REGISTERS:
        REGISTERS[y] = REGISTERS[x]
    else:
        REGISTERS[y] = int(x)
    CURRENT_INSTRUCTION += 1
    
def inc(x):
    global CURRENT_INSTRUCTION
    REGISTERS[x] += 1
    CURRENT_INSTRUCTION += 1
    
def dec(x):
    global CURRENT_INSTRUCTION
    REGISTERS[x] -= 1
    CURRENT_INSTRUCTION += 1

def jnz(x, y):
    global CURRENT_INSTRUCTION
    x_val = REGISTERS[x] if x in REGISTERS else int(x)
    y_val = REGISTERS[y] if y in REGISTERS else int(y)
    
    if x_val != 0:
        CURRENT_INSTRUCTION += y_val
    else:
        CURRENT_INSTRUCTION += 1    
    
def part1(input):
    instructions = []
    
    for line in input:
        line = line.strip()
        instructions.append(line)
        
    while CURRENT_INSTRUCTION < len(instructions):
        instruction = instructions[CURRENT_INSTRUCTION]
        
        parts = instruction.split(" ")
        if parts[0] == "cpy":
            copy(parts[1], parts[2])
        elif parts[0] == "inc":
            inc(parts[1])
        elif parts[0] == "dec":
            dec(parts[1])
        elif parts[0] == "jnz":
            jnz(parts[1], parts[2])
        
    return REGISTERS['a']

def part2(input):
    instructions = []
    
    global CURRENT_INSTRUCTION
    CURRENT_INSTRUCTION = 0
    
    REGISTERS['a'] = 0
    REGISTERS['b'] = 0
    REGISTERS['c'] = 1
    REGISTERS['d'] = 0
    
    for line in input:
        line = line.strip()
        instructions.append(line)
        
    while CURRENT_INSTRUCTION < len(instructions):
        instruction = instructions[CURRENT_INSTRUCTION]
        
        parts = instruction.split(" ")
        if parts[0] == "cpy":
            copy(parts[1], parts[2])
        elif parts[0] == "inc":
            inc(parts[1])
        elif parts[0] == "dec":
            dec(parts[1])
        elif parts[0] == "jnz":
            jnz(parts[1], parts[2])
            
    return REGISTERS['a']
    

if __name__ == "__main__":
    main()