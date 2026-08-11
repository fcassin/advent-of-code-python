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
    for line in input:
        line = line.strip()
        
        print(line)
        
    return 0

def part2(input):
    return 0

if __name__ == "__main__":
    main()
