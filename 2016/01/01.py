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

def main():
    with open("input.txt", "r") as input_file:
        print(part1(input_file.readlines()))

    with open("input.txt", "r") as input_file:
        print(part2(input_file.readlines()))

def walk(instructions):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    x, y = 0, 0
    direction = 0
    
    for instruction in instructions:
        turn = instruction[0]
        distance = int(instruction[1:])
        
        if turn == 'R':
            direction = (direction + 1) % 4
        elif turn == 'L':
            direction = (direction - 1) % 4
        
        dx, dy = directions[direction]
        x += dx * distance
        y += dy * distance
        
    return (x, y)

def visit(instructions):
    visited = set()
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    x, y = 0, 0
    direction = 0
    
    visited.add((x, y))
    for instruction in instructions:
        turn = instruction[0]
        distance = int(instruction[1:])
        
        if turn == 'R':
            direction = (direction + 1) % 4
        elif turn == 'L':
            direction = (direction - 1) % 4
        
        dx, dy = directions[direction]
        for _ in range(distance):
            x += dx
            y += dy
            
            if (x, y) in visited:
                return (x, y)
            
            visited.add((x, y))
    
    return None

def part1(input):
    destination = walk(input[0].strip().split(", "))

    return grid.manhattan(destination)

def part2(input):
    destination = visit(input[0].strip().split(", "))
    print(destination)

    return grid.manhattan(destination)

if __name__ == "__main__":
    main()