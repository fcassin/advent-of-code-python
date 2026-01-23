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
    
def is_pickable(map, x, y):
    neighbours = 0
    
    if map[x][y] != '@':
        return False
    
    for dx, dy in [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]:
        if 0 <= x + dx < len(map):
            if 0 <= y + dy < len(map[x]):
                if map[x+dx][y+dy] == '@':
                    neighbours = neighbours + 1          
                    
    return neighbours < 4  
    
def part1(input):
    map = collections.defaultdict(lambda: collections.defaultdict(str))
    
    for y, line in enumerate(input):
        line = line.strip()
        
        for x, char in enumerate(line):
            map[x][y] = char
        
    total = 0
    for x in map:
        for y in map:
            if is_pickable(map, x, y):
                total = total + 1
        
    return total

def part2(input):
    map = collections.defaultdict(lambda: collections.defaultdict(str))
    
    for y, line in enumerate(input):
        line = line.strip()
        
        for x, char in enumerate(line):
            map[x][y] = char
        
    total = 0
    pickables = []
    pickable_count = 0
    for x in map:
        for y in map:
            if is_pickable(map, x, y):
                pickable_count = pickable_count + 1
                pickables.append((x, y))
                
    total = total + pickable_count
    while pickable_count > 0:
        #print(f"removed {pickable_count} rolls of paper")
        for pickable in pickables:
            map[pickable[0]][pickable[1]] = '.'
            
        pickables = []
        pickable_count = 0
        for x in map:
            for y in map:
                if is_pickable(map, x, y):
                    pickable_count = pickable_count + 1
                    pickables.append((x, y))
                        
        total = total + pickable_count
        
    return total

if __name__ == "__main__":
    main()