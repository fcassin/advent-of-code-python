import collections
import functools
import itertools
import hashlib

from aoc import graph, ints, letter


def main():
    with open("input.txt", "r") as input_file:
        print(part1(input_file.readlines()))

    with open("input.txt", "r") as input_file:
        print(part2(input_file.readlines()))

def compute(instructions, registers):
    pointer = 0
    while pointer < len(instructions):
        raw = instructions[pointer]
        
        if ', ' in raw:
            raw, offset = raw.split(', ')
            offset = int(offset)
            
        instruction, register = raw.split(' ')
        
        if instruction == 'jmp':
            offset = int(register)
            register = None
        
        if instruction == 'hlf':
            registers[register] //= 2
            pointer += 1
        elif instruction == 'tpl':
            registers[register] *= 3
            pointer += 1
        elif instruction == 'inc':
            registers[register] += 1
            pointer += 1
        elif instruction == 'jmp':
            pointer += offset
        elif instruction == 'jie':
            if registers[register] % 2 == 0:
                pointer += offset
            else:
                pointer += 1
        elif instruction == 'jio':
            if registers[register] == 1:
                pointer += offset
            else:
                pointer += 1

    return registers

def part1(input):
    instructions = []
    
    for line in input:
        instructions.append(line.strip())
    
    registers = {'a': 0, 'b': 0}
        
    registers = compute(instructions, registers)
        
    return registers['b']

def part2(input):
    instructions = []
    
    for line in input:
        instructions.append(line.strip())
    
    registers = {'a': 1, 'b': 0}
        
    registers = compute(instructions, registers)
        
    return registers['b']

if __name__ == "__main__":
    main()
