import sys
sys.path.append("../../")

import collections
import functools
import graph
import grid
import ints
import itertools
import letter
import hashlib
import screen

def main():
    with open("input.txt", "r") as input_file:
        print(part1(input_file.readlines()))

    with open("input.txt", "r") as input_file:
        print(part2(input_file.readlines()))
    
def part1(input):
    fresh_total = 0
    parsing_ranges = True
    ranges = []
    for line in input:
        line = line.strip()
        
        if line == "":
            parsing_ranges = False
            continue
        
        if parsing_ranges:
            parts = line.split("-")
            ranges.append((int(parts[0]), int(parts[1])))
        else:
            value = int(line)
            for range in ranges:
                if range[0] <= value <= range[1]:
                    fresh_total += 1 
                    break
        
    return fresh_total

def part2(input):
    parsing_ranges = True
    ranges = []
    for line in input:
        line = line.strip()
        
        if line == "":
            parsing_ranges = False
            continue
        
        if parsing_ranges:
            parts = line.split("-")
            ranges.append((int(parts[0]), int(parts[1])))
    
    merged = True
    while merged:
        merged = False
        ranges = sorted(ranges)
        
        for index in range(len(ranges)):
            if index < len(ranges) - 1:
                current = ranges[index]
                next = ranges[index + 1]
                
                if next[0] - 1 <= current[1]:
                    ranges.remove(current)
                    ranges.remove(next)
                    
                    end_of_range = max(current[1], next[1])
                    # end_of_range = next[1]
                    
                    ranges.insert(0, (current[0], end_of_range))
                    index = index - 1
                    merged = True
                    
    total = 0
    for current in ranges:
        diff = (current[1] - current[0]) + 1
        total = total + diff
        
    # Too low: 346934484731209
    # Too low: 346934484731226
    # Correct: 357485433193284
    return total

if __name__ == "__main__":
    main()