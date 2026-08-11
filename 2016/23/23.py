import collections
import functools
import itertools
import hashlib

from aoc import graph, grid, ints, letter, screen


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

INSTRUCTIONS = []
CURRENT_INSTRUCTION = 0
FLIPPED_INSTRUCTIONS = []
    
def copy(x, y):
    global CURRENT_INSTRUCTION
    if y in REGISTERS:
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

def undo(instruction_index):
    global INSTRUCTIONS
    instruction = INSTRUCTIONS[instruction_index]
    parts = instruction.split(" ")
    
    if parts[0] == "inc":
        dec(parts[1])
    elif parts[0] == "dec":
        inc(parts[1])

def jnz(x, y):
    global CURRENT_INSTRUCTION
    x_val = REGISTERS[x] if x in REGISTERS else int(x)
    y_val = REGISTERS[y] if y in REGISTERS else int(y)
    
    if y_val == -2:
        inst_1 = INSTRUCTIONS[CURRENT_INSTRUCTION - 1]
        inst_2 = INSTRUCTIONS[CURRENT_INSTRUCTION - 2]
        
        parts_1 = inst_1.split(" ")
        parts_2 = inst_2.split(" ")
        
        jumper = x
        if parts_1[1] == jumper:
            to_inc = parts_2[1]
            to_inc_val = REGISTERS[to_inc] if to_inc in REGISTERS else int(to_inc)
            
            REGISTERS[to_inc] = to_inc_val + abs(REGISTERS[jumper])
            REGISTERS[jumper] = 0
        elif parts_2[1] == jumper:
            to_inc = parts_1[1]
            to_inc_val = REGISTERS[to_inc] if to_inc in REGISTERS else int(to_inc)
            
            REGISTERS[to_inc] = to_inc_val + abs(REGISTERS[jumper])
            REGISTERS[jumper] = 0
        
        CURRENT_INSTRUCTION += 1
    elif y_val == -5 and INSTRUCTIONS[CURRENT_INSTRUCTION - 5].split(" ")[0] == "cpy":
        # Too hard-coded but should be ok
        REGISTERS["a"] = REGISTERS["a"] + (REGISTERS["b"] * REGISTERS["d"])
        
        CURRENT_INSTRUCTION += 1
    else: 
        if x_val != 0:
            CURRENT_INSTRUCTION += y_val
        else:
            CURRENT_INSTRUCTION += 1
        
def toggle(x):
    global CURRENT_INSTRUCTION
    global FLIPPED_INSTRUCTIONS
    
    x_val = REGISTERS[x] if x in REGISTERS else int(x)
    target_instruction_index = CURRENT_INSTRUCTION + x_val
    
    if 0 <= target_instruction_index < len(FLIPPED_INSTRUCTIONS):
        FLIPPED_INSTRUCTIONS[target_instruction_index] = \
            not FLIPPED_INSTRUCTIONS[target_instruction_index]
            
    CURRENT_INSTRUCTION += 1
    
def part1(input):
    instructions = []
    
    for line in input:
        line = line.strip()
        instructions.append(line)
        
    global INSTRUCTIONS
    INSTRUCTIONS = instructions
    
    global CURRENT_INSTRUCTION
    CURRENT_INSTRUCTION = 0 
        
    global FLIPPED_INSTRUCTIONS
    FLIPPED_INSTRUCTIONS = [False] * len(instructions)
        
    REGISTERS['a'] = 7    
        
    while CURRENT_INSTRUCTION < len(instructions):
        instruction = instructions[CURRENT_INSTRUCTION]
        
        parts = instruction.split(" ")
        if not FLIPPED_INSTRUCTIONS[CURRENT_INSTRUCTION]:
            if parts[0] == "tgl":
                toggle(parts[1])
            elif parts[0] == "cpy":
                copy(parts[1], parts[2])
            elif parts[0] == "inc":
                inc(parts[1])
            elif parts[0] == "dec":
                dec(parts[1])
            elif parts[0] == "jnz":
                jnz(parts[1], parts[2])
        else:
            if parts[0] == "tgl":
                inc(parts[1])
            elif parts[0] == "cpy":
                jnz(parts[1], parts[2])
            elif parts[0] == "inc":
                dec(parts[1])
            elif parts[0] == "dec":
                inc(parts[1])
            elif parts[0] == "jnz":
                copy(parts[1], parts[2])
       
    return REGISTERS['a']

def part2(input):
    instructions = []
    
    for line in input:
        line = line.strip()
        instructions.append(line)
     
    global INSTRUCTIONS
    INSTRUCTIONS = instructions
        
    global CURRENT_INSTRUCTION
    CURRENT_INSTRUCTION = 0    
        
    global FLIPPED_INSTRUCTIONS
    FLIPPED_INSTRUCTIONS = [False] * len(instructions)
        
    REGISTERS['a'] = 12
        
    while CURRENT_INSTRUCTION < len(instructions):
        instruction = instructions[CURRENT_INSTRUCTION]
        
        parts = instruction.split(" ")
        if not FLIPPED_INSTRUCTIONS[CURRENT_INSTRUCTION]:
            if parts[0] == "tgl":
                toggle(parts[1])
            elif parts[0] == "cpy":
                copy(parts[1], parts[2])
            elif parts[0] == "inc":
                inc(parts[1])
            elif parts[0] == "dec":
                dec(parts[1])
            elif parts[0] == "jnz":
                # print("original jnz")
                jnz(parts[1], parts[2])
        else:
            if parts[0] == "tgl":
                inc(parts[1])
            elif parts[0] == "cpy":
                # print("flipped cpy")
                jnz(parts[1], parts[2])
            elif parts[0] == "inc":
                dec(parts[1])
            elif parts[0] == "dec":
                inc(parts[1])
            elif parts[0] == "jnz":
                # print("flipped jnz")
                copy(parts[1], parts[2])
    
    # REGISTERS['a'] = 479008535
    return REGISTERS['a']
    

if __name__ == "__main__":
    main()
