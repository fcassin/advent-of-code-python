import collections
import itertools
import hashlib

from aoc import graph, ints, letter


def main():
    with open("input.txt", "r") as input_file:
        print(part1(input_file.readlines()))

    with open("input.txt", "r") as input_file:
        print(part2(input_file.readlines()))

target_sue = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
}

def is_valid_sue(sue, target_sue):
    for key, value in sue.items():
        if key not in target_sue or target_sue[key] != value:
            return False
    return True

def is_valid_sue_2(sue, target_sue):
    for key, value in sue.items():
        if key == "cats" or key == "trees":
            if key not in target_sue or value <= target_sue[key]:
                return False
        elif key == "pomeranians" or key == "goldfish":
            if key not in target_sue or value >= target_sue[key]:
                return False
        elif key not in target_sue or target_sue[key] != value:
            return False
    return True

def part1(input):
    for index, line in enumerate(input):
        line = line.replace('\n', '')
        line = line.replace(' ', '')
        line = line.split(':', 1)[1]
        
        values = line.split(',')
        
        sue = {}
        for value in values:
            key, val = value.split(':')
            sue[key] = int(val)
        
        if is_valid_sue(sue, target_sue):
            return index + 1
        
    return 0

def part2(input):
    for index, line in enumerate(input):
        line = line.replace('\n', '')
        line = line.replace(' ', '')
        line = line.split(':', 1)[1]

        values = line.split(',')
        
        sue = {}
        for value in values:
            key, val = value.split(':')
            sue[key] = int(val)
        
        if is_valid_sue_2(sue, target_sue):
            return index + 1
        
    return 0

if __name__ == "__main__":
    main()
