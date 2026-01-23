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
    start = None
    map = collections.defaultdict(lambda: collections.defaultdict(str))
    
    for y, line in enumerate(input):
        line = line.strip()
        
        for x, char in enumerate(line):
            map[x][y] = char
            
            if char == "S":
                start = (x, y)
        
    grid.display(map)
    print(start)
    
    splits = 0
    current_row = 0
    
    print(len(map), len(map[0]))
    while current_row < len(map[0]):
        print("Processing row:", current_row)
        
        if current_row != len(map[0]) - 1:
        
            for x in range(len(map)):
                if map[x][current_row] == "S" or map[x][current_row] == "|":
                    if map[x][current_row + 1] == "^":
                        map[x - 1][current_row + 1] = "|"
                        map[x + 1][current_row + 1] = "|"
                        splits += 1
                    else:
                        map[x][current_row + 1] = "|"
        
        current_row += 1
        
    grid.display(map)
    
    return splits

def part2(input):
    start = None
    map = collections.defaultdict(lambda: collections.defaultdict(str))
    
    for y, line in enumerate(input):
        line = line.strip()
        
        for x, char in enumerate(line):
            if char == "S":
                start = (x, y)
                map[x][y] = 1
            elif char == ".":
                map[x][y] = 0
            else:
                map[x][y] = -1
        
    grid.display(map)
    print(start)
    
    current_row = 0
    
    print(len(map), len(map[0]))
    while current_row < len(map[0]):
        print("Processing row:", current_row)
        
        if current_row != len(map[0]) - 1:
        
            for x in range(len(map)):
                if map[x][current_row] > 0:
                    if map[x][current_row + 1] == -1:
                        map[x - 1][current_row + 1] = map[x - 1][current_row + 1] + map[x][current_row]
                        map[x + 1][current_row + 1] = map[x + 1][current_row + 1] + map[x][current_row]
                    else:
                        map[x][current_row + 1] = map[x][current_row + 1] + map[x][current_row]
        
        current_row += 1
        
    realities = 0
    for x in range(len(map)):
        y = len(map[0]) - 1
        
        realities = realities + map[x][y]
        
    grid.display(map)
    
    return realities

if __name__ == "__main__":
    main()