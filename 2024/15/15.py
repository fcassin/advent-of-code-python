import collections
import copy
import functools
import itertools
import hashlib
import re

from aoc import graph, grid, letter


inputs = []
map = collections.defaultdict(lambda:collections.defaultdict(str))

def main():
    with open("input.txt", "r") as input_file:
        lines = input_file.readlines()
        print(part1(lines))
        print(part2(lines))

def move(pos, input):
    directions = {
        "<": (-1, 0),
        "^": (0, -1),
        "v": (0, 1),
        ">": (1, 0),
    }

    direction = directions[input]

    if map[pos[0] + direction[0]][pos[1] + direction[1]] == "#":
        return pos
    elif map[pos[0] + direction[0]][pos[1] + direction[1]] == ".":
        map[pos[0]][pos[1]] = "."
        map[pos[0] + direction[0]][pos[1] + direction[1]] = "@"
        
        return (pos[0] + direction[0], pos[1] + direction[1])
    elif map[pos[0] + direction[0]][pos[1] + direction[1]] == "O":
        current_pos = (pos[0] + direction[0], pos[1] + direction[1])

        while map[current_pos[0]][current_pos[1]] == "O":
            current_pos = (current_pos[0] + direction[0], current_pos[1] + direction[1])

        if map[current_pos[0]][current_pos[1]] == "#":
            return pos
        
        if map[current_pos[0]][current_pos[1]] == ".":
            map[current_pos[0]][current_pos[1]] = "O"
            while current_pos[0] != pos[0] and current_pos[1] != pos[1]:
                map[current_pos[0]][current_pos[1]] = "O"
                current_pos = (current_pos[0] - direction[0], current_pos[1] - direction[1])

            map[pos[0]][pos[1]] = "."
            map[pos[0] + direction[0]][pos[1] + direction[1]] = "@"

            return (pos[0] + direction[0], pos[1] + direction[1])
        
def move_boxes(pos, input):
    directions = {
        "<": (-1, 0),
        "^": (0, -1),
        "v": (0, 1),
        ">": (1, 0),
    }

    direction = directions[input]

    if map[pos[0] + direction[0]][pos[1] + direction[1]] == "#":
        return pos
    
    elif map[pos[0] + direction[0]][pos[1] + direction[1]] == ".":
        map[pos[0]][pos[1]] = "."
        map[pos[0] + direction[0]][pos[1] + direction[1]] = "@"
        
        return (pos[0] + direction[0], pos[1] + direction[1])
    
    elif map[pos[0] + direction[0]][pos[1] + direction[1]] == "[" or map[pos[0] + direction[0]][pos[1] + direction[1]] == "]":
        movables = set()

        if input == "^" or input == "v":
            if map[pos[0] + direction[0]][pos[1] + direction[1]] == "[":
                movables.add((pos[0] + direction[0], pos[1] + direction[1], "["))
                movables.add((pos[0] + direction[0] + 1, pos[1] + direction[1], "]"))
            elif map[pos[0] + direction[0]][pos[1] + direction[1]] == "]":
                movables.add((pos[0] + direction[0], pos[1] + direction[1], "]"))
                movables.add((pos[0] + direction[0] - 1, pos[1] + direction[1], "["))
        else:
            movables.add((pos[0] + direction[0], pos[1] + direction[1], map[pos[0] + direction[0]][pos[1] + direction[1]]))

        # print("movables:", movables)
        # print("movables:", movables)
        # print("movables:", movables)

        
        can_move = True

        # might need to remember the value in the movable
        entire_movables = set()
        entire_movables.update(movables)
        # print(movables)
        # print(entire_movables)

        while True:
            rest = True
            new_movables = set()
            
            for movable in movables:
                if map[movable[0] + direction[0]][movable[1] + direction[1]] == "#":
                    return pos
                elif map[movable[0] + direction[0]][movable[1] + direction[1]] == "[" or map[movable[0] + direction[0]][movable[1] + direction[1]] == "]":
                    if input == "^" or input == "v":
                        if map[movable[0] + direction[0]][movable[1] + direction[1]] == "[":
                            new_movables.add((movable[0] + direction[0], movable[1] + direction[1], "["))
                            new_movables.add((movable[0] + direction[0] + 1, movable[1] + direction[1], "]"))
                        elif map[movable[0] + direction[0]][movable[1] + direction[1]] == "]":
                            new_movables.add((movable[0] + direction[0], movable[1] + direction[1], "]"))
                            new_movables.add((movable[0] + direction[0] - 1, movable[1] + direction[1], "["))
                    else:
                        new_movables.add((movable[0] + direction[0], movable[1] + direction[1], map[movable[0] + direction[0]][movable[1] + direction[1]]))
                        pass
                    rest = False

            movables = new_movables
            entire_movables.update(movables)

            # print(new_movables)
            # print("entire_movables:", entire_movables)

            if rest == True:
                break       

        # print("found a resting place")
        # print("found a resting place")
        # print("found a resting place")
        # print(entire_movables)

        for movable in entire_movables:
            map[movable[0]][movable[1]] = "."
        for movable in entire_movables:            
            map[movable[0] + direction[0]][movable[1] + direction[1]] = movable[2]

        map[pos[0]][pos[1]] = "."
        map[pos[0] + direction[0]][pos[1] + direction[1]] = "@"

        return (pos[0] + direction[0], pos[1] + direction[1])

def part1(input):
    count = 0

    start = (0,0)

    reading_map = True
    for y, line in enumerate(input):
        line = line.replace('\n', '')
        if line != None:
            if line == "":
                reading_map = False
                continue
            
            if reading_map:
                for x, char in enumerate(line):
                    map[x][y] = char

                    if char == "@":
                        start = (x, y)

            if not reading_map:
                for input in line:
                    inputs.append(input)
                

    # grid.display(map)

    position = start
    for input in inputs:
        position = move(position, input)
        # print("Move", input)
        # grid.display(map)
        # print()

    for x in map:
        for y in map[x]:
            if map[x][y] == "O":
                count += 100 * y + x

    grid.display(map)

    return count

def part2(input):
    count = 0

    map.clear()
    inputs.clear()

    start = (0,0)

    reading_map = True
    for y, line in enumerate(input):
        line = line.replace('\n', '')
        if line != None:
            if line == "":
                reading_map = False
                continue
            
            if reading_map:
                for x, char in enumerate(line):
                    if char == "#":
                        map[x * 2][y] = "#"
                        map[x * 2 + 1][y] = "#"
                    elif char == "O":
                        map[x * 2][y] = "["
                        map[x * 2 + 1][y] = "]"
                    elif char == ".":
                        map[x * 2][y] = "."
                        map[x * 2 + 1][y] = "."
                    elif char == "@":
                        start = (x * 2, y)
                        map[x * 2][y] = "@"
                        map[x * 2 + 1][y] = "."

            if not reading_map:
                for input in line:
                    inputs.append(input)

    position = start
    for input in inputs:
        position = move_boxes(position, input)
        # print("Move", input)
        # grid.display(map)
        # print()

    grid.display(map)

    for x in map:
        for y in map[x]:
            if map[x][y] == "[":
                count += 100 * y + x

    return count

if __name__ == "__main__":
    main()
