import collections
import copy
import functools
import hashlib
import re

from aoc import graph, grid, letter


lab = collections.defaultdict(lambda:collections.defaultdict(str))

next_dir = {
    (0, -1): (1, 0),
    (1, 0): (0, 1),
    (0, 1): (-1, 0),
    (-1, 0): (0, -1)
}

def walk(lab, position, direction, seen, seen_dir):
    x, y = position[0], position[1]

    while 0 <= x < len(lab) and 0 <= y < len(lab[0]):
        x, y = position[0], position[1]

        if (position, direction) in seen_dir:
            return 0, True

        if lab[x + direction[0]][y + direction[1]] == "." or lab[x + direction[0]][y + direction[1]] == "^":
            position = (x + direction[0], y + direction[1])
            if lab[x + direction[0]][y + direction[1]] == ".":
                seen.add(position)
                seen_dir.add(((x, y), direction))

        elif lab[x + direction[0]][y + direction[1]] == "#":
            direction = next_dir[direction]

        elif lab[x + direction[0]][y + direction[1]] == "":
            position = (x + direction[0], y + direction[1])
            if lab[x + direction[0]][y + direction[1]] == ".":
                seen.add(position)
                seen_dir.add(((x, y), direction))
            return len(seen), False

        else:
            print(lab[x + direction[0]][y + direction[1]])

    return len(seen), False

start_direction = (0, -1)
start_position = (0, 0)

seen = set()
seen_dir = set()

def part1(input):
    global start_position

    for y, line in enumerate(input):
        line = line.replace('\n', '')
        if line != None:
            for x, char in enumerate(line):
                if char == "^":
                    lab[x][y] = "."
                    start_position = (x, y)
                    continue    
                
                lab[x][y] = char

    direction = start_direction
    position = start_position
    
    seen.add(start_position)
    
    walked, _ = walk(lab, position, direction, seen, seen_dir)

    return walked

def part2(input):
    count = 0

    # grid.display(lab)

    rows = len(lab)
    columns = len(lab[0])

    print(len(seen))

    for r in range(rows):
        for c in range(columns):
            if lab[r][c] == "." and (r, c) in seen:
                lab[r][c] = "#"
                _, loops = walk(lab, start_position, start_direction, set(), set())
                
                if loops:
                    if (r,c) != start_position:
                        count = count + 1
                lab[r][c] = "."

    return count

def main():
    with open("input.txt", "r") as input_file:
        print(part1(input_file.readlines()))

    with open("input.txt", "r") as input_file:
        print(part2(input_file.readlines()))

if __name__ == "__main__":
    main()
