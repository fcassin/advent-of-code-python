import collections
import copy
import functools
import itertools
import hashlib
import re

from aoc import graph, grid, letter


map = collections.defaultdict(lambda:collections.defaultdict(str))

def main():
    with open("input.txt", "r") as input_file:
        lines = input_file.readlines()
        print(part1(lines))
        print(part2(lines))

def valid_step(map, current, next):
    width = len(map)
    height = len(map[0])

    if next[0] >= 0 and next[0] < width and next[1] >= 0 and next[1] < height:
        if map[next[0]][next[1]] == ".":
            return False
        
        current_value = int(map[current[0]][current[1]])
        next_value = int(map[next[0]][next[1]])

        if current_value + 1 == next_value:
            return True
        
    return False

def reachable_endpoints(paths):
    reachable = set()
    for path in paths:
        end = path[len(path) - 1]
        value = 10 * end[0] + end[1]
        reachable.add(value)
    return len(reachable)

valid_paths = []

def part1(input):
    starting_coordinates = []

    for y, line in enumerate(input):
        line = line.replace('\n', '')
        if line != None:
            for x, char in enumerate(line):
                map[x][y] = char

                if char == '0':
                    starting_coordinates.append((x,y))

    # grid.display(map)
    
    target = "9"
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    sum = 0
    for starting_coordinate in starting_coordinates:
        ps = grid.depth_first_search(map, valid_step, directions, starting_coordinate, target)
        sum += reachable_endpoints(ps)
        valid_paths.extend(ps)

    return sum

def part2(input):
    return len(valid_paths)

if __name__ == "__main__":
    main()
