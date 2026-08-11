import collections
import copy
import functools
import itertools
import hashlib
import re

from aoc import graph, grid, letter


map = collections.defaultdict(lambda:collections.defaultdict(str))

def main():
    with open("input.txt", "r") as input_file:
        lines = input_file.readlines()
        print(part1(lines))
        print(part2(lines))

def len_stones(values, remaining):
    sum = 0

    for value in values:
        sum += len_stone(value, remaining)

    return sum

@functools.cache
def len_stone(value, remaining):
    if remaining == 0:
        return 1
    
    if value == 0:
        new_value = 1
        length = len_stone(new_value, remaining-1)
                
    elif len(str(value)) % 2 == 0:
        value = str(value)
        left, right = str(value)[:len(str(value))//2], value[len(str(value))//2:]

        length = len_stones([int(left), int(right)], remaining-1)

    else:
        new_value = 2024 * value
        length = len_stone(new_value, remaining-1)

    return length

def part1(input):
    stones = []
    for line in input:
        line = line.replace('\n', '')
        if line != None:
            for value in line.split():
                stones.append(int(value))

    length = len_stones(stones, 25)

    return length

def part2(input):
    stones = []
    for line in input:
        line = line.replace('\n', '')
        if line != None:
            for value in line.split():
                stones.append(int(value))

    length = len_stones(stones, 75)

    return length

if __name__ == "__main__":
    main()
