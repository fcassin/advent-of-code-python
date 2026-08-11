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
    
def part1(input):
    pos = 50
    count = 0
    
    for line in input:
        line = line.strip()
        
        value = ints.extract(line)
        
        if line.startswith("L"):
            pos = (pos - value[0]) % 100
            if pos == 0:
                count += 1
        elif line.startswith("R"):
            pos = (pos + value[0]) % 100
            if pos == 0:
                count += 1
        
    return count

def part2(input):
    pos = 50
    count = 0
    
    for line in input:
        line = line.strip()
        
        value = ints.extract(line)
        displacement = value[0]
        
        if displacement > 100:
            count = count + (displacement // 100)
            displacement = displacement % 100
        
        if line.startswith("L"):
            start = pos
            pos = pos - displacement
            if pos == 0:
                count += 1
            elif pos < 0 and start != 0:
                pos = pos % 100
                count += 1
            elif pos < 0:
                pos = pos % 100
                    
        elif line.startswith("R"):
            start = pos
            pos = pos + displacement
            if pos == 100:
                pos = 0
                count += 1
            elif start != 0 and pos > 100:
                pos = pos % 100
                count += 1
            elif pos > 100:
                pos = pos % 100
        
    return count

if __name__ == "__main__":
    main()
