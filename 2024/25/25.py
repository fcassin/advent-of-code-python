
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

def part1(input):
    locks = []
    keys = []
    
    index = 0
    while index < len(input):
        line = input[index]
        line = line.replace('\n', '')
        if line != None:
            if line == "":
                index = index + 1
                continue
            elif line == ".....":
                key = [-1, -1, -1, -1 ,-1]
                for x in range(7):
                    next_line = input[index + x]
                    for y in range(5):
                        if key[y] == -1 and next_line[y] == "#":
                            key[y] = 6 - x

                keys.append(key)

                index = index + 7
                continue
            elif line == "#####":
                lock = [-1, -1, -1, -1 ,-1]
                for x in range(7):
                    next_line = input[index + x]
                    for y in range(5):
                        if lock[y] == -1 and next_line[y] == ".":
                            lock[y] = x - 1

                locks.append(lock)

                index = index + 7
                continue

    sum = 0
    for lock in locks:
        for key in keys:
            if lock[0] + key[0] < 6 and lock[1] + key[1] < 6 and lock[2] + key[2] < 6 and lock[3] + key[3] < 6 and lock[4] + key[4] < 6:
                sum += 1

    return sum

def part2(input):
    return 0

if __name__ == "__main__":
    main()