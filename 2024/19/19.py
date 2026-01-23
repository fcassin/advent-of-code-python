import sys
sys.path.append("../../")

import collections
import copy
import functools
import graph
import grid
import itertools
import letter
import hashlib
import re

map = collections.defaultdict(lambda: collections.defaultdict(str))

def main():
    with open("input.txt", "r") as input_file:
        lines = input_file.readlines()
        print(part1(lines))
        print(part2(lines))

def max_length(towels):
    max_len = 0        
    for towel in towels:
        if len(towel) > max_len:
            max_len = len(towel)
    return max_len

impossibles = set()
possibles = {}
def possible(design, towels):
    count = 0

    if design == "":
        return True, 1
    
    if design in possibles:
        return True, possibles[design]

    acc = ""
    max_len = max_length(towels)

    possibilities = []
    for color in design:
        acc = acc + color

        if len(acc) > max_len:
            break

        if acc in towels:
            possibilities.append(design[len(acc):])

    # print(possibilities)
    pos = False
    for possibility in possibilities:
        if possibility in impossibles:
            continue
        
        p, ways = possible(possibility, towels)
        if not p:
            impossibles.add(possibility)

        # 

        possibles[possibility] = ways
        # print(possibles)
        
        pos = pos or p
        
        count += ways

    return pos, count



# seen = set()
# def possible(design, towels):
#     if design == "":
#         return True
# 
#     acc = ""
#     max_len = max_length(towels)
# 
#     possibilities = []
#     for color in design:
#         acc = acc + color
# 
#         if len(acc) > max_len:
#             break
# 
#         if acc in towels:
#             possibilities.append(design[len(acc):])
# 
#     # print(possibilities)
#     pos = False
#     for possibility in possibilities:
#         if possibility in seen:
#             continue
#         
#         p = possible(possibility, towels)
#         if not p:
#             seen.add(possibility)
# 
#         pos = pos or p
#         if pos:
#             return pos
# 
#     return pos

def part1(input):
    reading_towels = True
    available_towels = set()
    designs = list()
    
    for line in input:
        line = line.replace('\n', '')
        if line != None:
            if reading_towels:
                available_towels = [x.strip() for x in line.split(",")]
                reading_towels = False

            elif line != "":
                designs.append(line)

   

    # def possible
    count = 0
    for design in designs:
        p, w = possible(design, available_towels) 
        print(design, p, w)

        if p:
            # count += 1
            count += w

    return count

def part2(input):
    return 0

if __name__ == "__main__":
    main()