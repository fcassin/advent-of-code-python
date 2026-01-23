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
import png
import screen
import z3

def main():
    with open("input.txt", "r") as input_file:
        print(part1(input_file.readlines()))

    with open("input.txt", "r") as input_file:
        print(part2(input_file.readlines()))

SHAPE_0 = """
.##
##.
###
"""

SHAPE_1 = """
..#
.##
###
"""

SHAPE_2 = """
###
###
#..
"""

SHAPE_3 = """
###
.#.
###
"""

SHAPE_4 = """
.##
##.
#..
"""

SHAPE_5 = """
###
#..
###
"""

def total_area(presents):
    area = 0
    
    for index, present in enumerate(presents):
        if index in [0, 2, 3, 5]:
            area = area + 7 * present
        else:
            area = area + 6 * present
            
    return area
        

def part1(input):
    possible_trees = 0
    
    for line in input:
        line = line.strip()
        
        dimensions, presents = line.split(": ")
        dimensions = ints.extract(dimensions)
        presents = ints.extract(presents)
        
        # print(dimensions, presents, dimensions[0] * dimensions[1], total_area(presents))
        
        if (total_area(presents) * 1.3) < dimensions[0] * dimensions[1]:
            # print(dimensions, presents, dimensions[0] * dimensions[1], total_area(presents))
            possible_trees = possible_trees + 1
        else:
            print("NO", dimensions, presents, dimensions[0] * dimensions[1], total_area(presents))
            pass
        
    return possible_trees

def part2(input):
    return 0
    

if __name__ == "__main__":
    main()