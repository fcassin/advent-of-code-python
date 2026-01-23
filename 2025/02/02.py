import sys
sys.path.append("../../")

import collections
import functools
import graph
import grid
import hashlib
import ints
import itertools
import letter
import math
import screen

def main():
    with open("input.txt", "r") as input_file:
        print(part1(input_file.readlines()))

    with open("input.txt", "r") as input_file:
        print(part2(input_file.readlines()))
    
def part1(input):
    total = 0
    
    for line in input:
        line = line.strip()
        
        ranges = line.split(',')
        for store_range in ranges:
            bounds = store_range.split('-')
            start = int(bounds[0])
            end = int(bounds[1])
            
            for value in range(start, end + 1):
                if len(str(value)) % 2 == 0:
                    half = len(str(value)) // 2
                    
                    if str(value)[:half] == str(value)[half:]:
                        total += value
        
    return total

def invalid_id(value):
    str_value = str(value)
    
    for step in range(1, len(str_value)//2 + 1):
        found = True
        
        if len(str_value) % step != 0:
            continue
        
        for index in range(0, len(str_value), step):
            start = str_value[0:step]
            window = str_value[index:index+step]
            
            if window != start:
                found = False
                break
            
        if found:
            return found
    
    return False

def part2(input):
    total = 0
    
    for line in input:
        line = line.strip()
        
        ranges = line.split(',')
        for store_range in ranges:
            bounds = store_range.split('-')
            start = int(bounds[0])
            end = int(bounds[1])
            
            for value in range(start, end + 1):
                if invalid_id(value):
                    total += value
        
    return total

if __name__ == "__main__":
    main()