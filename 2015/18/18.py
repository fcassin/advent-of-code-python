import collections
import functools
import itertools
import hashlib
import os
import time

from aoc import graph, ints, letter


def main():
    with open("input.txt", "r") as input_file:
        print(part1(input_file.readlines()))

    with open("input.txt", "r") as input_file:
        print(part2(input_file.readlines()))

global map
map = collections.defaultdict(lambda: collections.defaultdict(int))

def display_map():
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[x][y] == 1:
                print('#', end='')
            else:
                print('.', end='')
        print()
    
def count_neighbors(x, y):
    count = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            
            if x + dx < 0 or x + dx >= len(map) or y + dy < 0 or y + dy >= len(map[0]):
                continue
            
            if map[x + dx][y + dy] == 1:
                count += 1
    return count

def animate():
    global map
    new_map = collections.defaultdict(lambda: collections.defaultdict(int))
    
    for y in range(len(map)):
        for x in range(len(map[0])):
            neighbors = count_neighbors(x, y)
            if map[x][y] == 1:
                if neighbors == 2 or neighbors == 3:
                    new_map[x][y] = 1
                else:
                    new_map[x][y] = 0
            elif map[x][y] == 0:
                if neighbors == 3:
                    new_map[x][y] = 1
                else:
                    new_map[x][y] = 0
                    
    map = new_map
    
def animate_always_on():
    global map
    new_map = collections.defaultdict(lambda: collections.defaultdict(int))
    
    for y in range(len(map)):
        for x in range(len(map[0])):
            
            if (x == 0 and y == 0) or (x == 0 and y == len(map[0]) - 1) or (x == len(map) - 1 and y == 0) or (x == len(map) - 1 and y == len(map[0]) - 1):
                new_map[x][y] = 1
            else:
                neighbors = count_neighbors(x, y)
                if map[x][y] == 1:
                    if neighbors == 2 or neighbors == 3:
                        new_map[x][y] = 1
                    else:
                        new_map[x][y] = 0
                elif map[x][y] == 0:
                    if neighbors == 3:
                        new_map[x][y] = 1
                    else:
                        new_map[x][y] = 0
                    
    map = new_map
    
def count_lights():
    count = 0
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[x][y] == 1:
                count += 1
    return count

def part1(input):
    for y, line in enumerate(input):
        line = line.replace('\n', '')
        for x, char in enumerate(line):
            if char == '#':
                map[x][y] = 1
            else:
                map[x][y] = 0
        
    for _ in range(100):    
        animate()
        
    return count_lights()

def part2(input):
    for y, line in enumerate(input):
        line = line.replace('\n', '')
        for x, char in enumerate(line):
            if char == '#':
                map[x][y] = 1
            else:
                map[x][y] = 0
        
    for _ in range(100):
        os.system('clear')
        display_map()
        time.sleep(0.3)
         
        animate_always_on()
        
    return count_lights()

if __name__ == "__main__":
    main()
