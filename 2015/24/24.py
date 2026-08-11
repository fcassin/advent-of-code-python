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

def part1(input):
    values = []
    
    for line in input:
        value = ints.extract_one(line)
        values.append(value)
    
    target = sum(values) // 3
    
    potential_combos = []
    for i in range(1, len(values)):
        for combo in itertools.combinations(values, i):
            if sum(combo) == target:
                product = functools.reduce(lambda x, y: x * y, combo)
                potential_combos.append((combo, product))
        if len(potential_combos) > 0:
            break
        
    potential_combos.sort(key=lambda x: x[1])
        
    return potential_combos[0][1]

def part2(input):
    values = []
    
    for line in input:
        value = ints.extract_one(line)
        values.append(value)
    
    target = sum(values) // 4
    
    potential_combos = []
    for i in range(1, len(values)):
        for combo in itertools.combinations(values, i):
            if sum(combo) == target:
                product = functools.reduce(lambda x, y: x * y, combo)
                potential_combos.append((combo, product))
        if len(potential_combos) > 0:
            break
        
    potential_combos.sort(key=lambda x: x[1])
        
    return potential_combos[0][1]

if __name__ == "__main__":
    main()
