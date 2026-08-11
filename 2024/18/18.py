import collections
import copy
import functools
import itertools
import hashlib
import re

from aoc import graph, grid, letter


map = collections.defaultdict(lambda: collections.defaultdict(str))

def main():
    with open("input.txt", "r") as input_file:
        lines = input_file.readlines()
        print(part1(lines))
        print(part2(lines))

# TODO move those cardinal directions to grid.py
# right, down, left, up
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def valid_step(map, current, next):
    width = len(map)
    height = len(map[0])

    if next[0] >= 0 and next[0] < width and next[1] >= 0 and next[1] < height:
        if map[next[0]][next[1]] == "#":
            return False
        
        return True
        
    return False

# manhattan distance
def dist_func(map, start, end):
    # TODO: abs might be required for a generic func
    return (end[0] - start[0]) + (end[1] - start[1])

def a_star(map, valid_func, distance_func, directions, start, end):
    paths = collections.deque([(start[0], start[1], 0)])
    seen = set()

    seen.add(start)

    while len(paths) > 0:
        path = paths.popleft()
        current = (path[0], path[1])
        travelled = path[2]

        candidates = []
        for direction in directions:
            next = (current[0] + direction[0], current[1] + direction[1])

            if next in seen:
                continue
            seen.add(next)

            if valid_func(map, current, next):
                candidates.append((distance_func(map, current, end), (next[0], next[1])))

                if (next[0], next[1]) == end:
                    return (next[0], next[1], travelled + 1)
        
        # sort and append
        candidates = sorted(candidates)
        # print("candidates:", candidates)
        for candidate in candidates:
            paths.append((candidate[1][0], candidate[1][1], travelled + 1))

    return None

def part1(input):
    dimension = 70
    falling = 1024

    width, height = dimension + 1, dimension + 1

    start = (0, 0)
    end = (dimension, dimension)

    

    for y in range(width):
        for x in range(height):
            map[x][y] = '.'
            
    for count, line in enumerate(input):
        line = line.replace('\n', '')
        if line != None:
            if count < falling:
                # print(count, line)
                x, y = [int(v) for v in line.split(",")]
                
                map[x][y] = "#"
            
    grid.display(map)

    x, y, len = a_star(map, valid_step, dist_func, directions, start, end)

    return len

def part2(input):
    dimension = 70
    falling = 1024

    width, height = dimension + 1, dimension + 1

    start = (0, 0)
    end = (dimension, dimension)

    

    for y in range(width):
        for x in range(height):
            map[x][y] = '.'
            
    for count, line in enumerate(input):
        line = line.replace('\n', '')
        if line != None:
            x, y = [int(v) for v in line.split(",")]
            map[x][y] = "#"

            if count > falling:
                if a_star(map, valid_step, dist_func, directions, start, end) == None:
                    print(x,y)
                    break

    return 0

if __name__ == "__main__":
    main()
