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
        
def pick_one(input, capacity):
    high_pos = 0
    high_char = 0
    
    for pos, char in enumerate(input):
        if pos < len(input) - capacity:
            if int(char) > high_char:
                high_char = int(char)
                high_pos = pos
                
    return str(high_char), input[high_pos + 1:]
         
def max_joltage(input, capacity):
    buffer = ""
    
    while capacity > 0:
        capacity = capacity - 1
        char, input = pick_one(input, capacity)
        
        buffer = buffer + char
        
    return int(buffer)
    
def part1(input):
    total = 0
    
    for line in input:
        line = line.strip()
        
        total = total + max_joltage(line, 2)
        
    return total

def part2(input):
    total = 0
    
    for line in input:
        line = line.strip()
        
        joltage = max_joltage(line, 12)
        
        total = total + joltage
        
    return total

if __name__ == "__main__":
    main()
