import sys
sys.path.append("../../")

import collections
import functools
import graph
import ints
import itertools
import letter
import hashlib

def main():
    with open("input.txt", "r") as input_file:
        print(part1(input_file.readlines()))

    with open("input.txt", "r") as input_file:
        print(part2(input_file.readlines()))

def is_valid_triangle(sides):
    if sides is None or len(sides) != 3:
        return False
        
    if sides[0] + sides[1] > sides[2] and \
        sides[1] + sides[2] > sides[0] and \
        sides[2] + sides[0] > sides[1]:
        return True
    return False

def part1(input):
    valid_count = 0
    for line in input:
        values = ints.extract(line)
        
        if is_valid_triangle(values):
            valid_count += 1
        
    return valid_count

def part2(input):
    valid_count = 0
    
    triangleA = []
    triangleB = []
    triangleC = []
    
    for line in input:
        values = ints.extract(line)
        
        if len(values) != 3:
            continue
        
        triangleA.append(values[0])
        triangleB.append(values[1])
        triangleC.append(values[2])
        
        if len(triangleA) == 3:
            if is_valid_triangle(triangleA):
                valid_count += 1
            triangleA = []
        
            if is_valid_triangle(triangleB):
                valid_count += 1
            triangleB = []
        
            if is_valid_triangle(triangleC):
                valid_count += 1
            triangleC = []
            
    return valid_count

if __name__ == "__main__":
    main()