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
    
class Disc:
    def __init__(self, modulo, position):
        self.modulo = modulo
        self.position = position
        
    def __repr__(self):
        return f"Disc(modulo={self.modulo}, position={self.position})"

def aligned(discs, time):
    for disc in discs:
        time += 1
        if (disc.position + time) % disc.modulo != 0:
            return False
    
    return True
    
def part1(input):
    discs = []
    
    for line in input:
        line = line.strip()
        
        _, modulo, _, position = ints.extract(line)
        disc = Disc(modulo, position)
        discs.append(disc)
        
    current_time = 0
    while True:
        if aligned(discs, current_time):
            break
        
        current_time += 1
        
    return current_time

def part2(input):
    discs = []
    
    for line in input:
        line = line.strip()
        
        _, modulo, _, position = ints.extract(line)
        disc = Disc(modulo, position)
        discs.append(disc)
        
    disc = Disc(11, 0)
    discs.append(disc)    
        
    current_time = 0
    while True:
        if aligned(discs, current_time):
            break
        
        current_time += 1
        
    return current_time

if __name__ == "__main__":
    main()
