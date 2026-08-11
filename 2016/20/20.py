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

class Range:
    def __init__(self, low, high):
        self.low = low
        self.high = high
        
    def __repr__(self):
        return f"Range({self.low}, {self.high})"

def part1(input):
    ranges = []
    
    for line in input:
        line = line.strip()
        line = line.replace('-', ' ')
        
        values = ints.extract(line)
        ranges.append(Range(values[0], values[1]))
        
    test_value = 1
    while True:
        is_blocked = False
        
        for r in ranges:
            if r.low <= test_value <= r.high:
                is_blocked = True
                test_value = r.high + 1
                continue
                
        if not is_blocked:
            break
        
    return test_value

def part2(input):
    ranges = []
    
    for line in input:
        line = line.strip()
        line = line.replace('-', ' ')
        
        values = ints.extract(line)
        ranges.append(Range(values[0], values[1]))
        
    count = 0
    test_value = 1
    while test_value <= 4294967295:
        is_blocked = False
        
        for r in ranges:
            if r.low <= test_value <= r.high:
                is_blocked = True
                test_value = r.high + 1
                continue
                
        if not is_blocked:
            count += 1
            test_value += 1
    
    return count

if __name__ == "__main__":
    main()
