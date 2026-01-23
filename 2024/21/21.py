
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

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def valid_step(map, next):
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

def breadth_first_search(grid, valid_func, directions, starting_coordinate, target):
    valid_paths = []

    start = [starting_coordinate]
    paths = [start]

    if grid[starting_coordinate[0]][starting_coordinate[1]] == target:
        return paths

    best = 100

    seen = set()
    while len(paths) > 0:
        path = paths.pop()
        current = path[len(path) - 1]

        if len(path) > best:
            continue

        for direction in directions:
            next = (current[0] + direction[0], current[1] + direction[1])
            
            if valid_func(grid, next):
                new_path = copy.deepcopy(path)
                new_path.append(next)

                if grid[next[0]][next[1]] == target:
                    best = len(new_path)
                    valid_paths.append(new_path)
                else:
                    if (next, direction) in seen:
                        continue
                    seen.add((next, direction))

                    paths = [new_path] + paths

    return valid_paths

@functools.cache
def keypad_search(starting_coordinate, target):
    valid_paths = []

    start = [starting_coordinate]
    paths = [start]

    if keypad[starting_coordinate[0]][starting_coordinate[1]] == target:
        return paths

    best = 100

    seen = set()
    while len(paths) > 0:
        path = paths.pop()
        current = path[len(path) - 1]

        if len(path) > best:
            continue

        for direction in directions:
            next = (current[0] + direction[0], current[1] + direction[1])
            
            if valid_step(keypad, next):
                new_path = copy.deepcopy(path)
                new_path.append(next)

                if keypad[next[0]][next[1]] == target:
                    best = len(new_path)
                    valid_paths.append(new_path)
                else:
                    if (next, direction) in seen:
                        continue
                    seen.add((next, direction))

                    paths = [new_path] + paths

    return valid_paths

def directions_to_instructions(paths):
    possibilities = []
    buffer = []

    for path in paths:
        previous = path[0]
        path = path[1:]

        for i in range(len(path)):
            current = path[i]
            move = (current[0] - previous[0], current[1] - previous[1])
                       
            if (move[0], move[1]) == (0, 1):
                buffer.append("v")
            elif (move[0], move[1]) == (1, 0):
                buffer.append(">")
            elif (move[0], move[1]) == (0, -1):
                buffer.append("^")
            elif (move[0], move[1]) == (-1, 0):
                buffer.append("<")

            previous = current
        
        buffer.append("A")
        possibilities.append("".join(buffer))
        buffer.clear()
    return possibilities

numpad_distance = {}

numpad = collections.defaultdict(lambda: collections.defaultdict(str))
keypad = collections.defaultdict(lambda: collections.defaultdict(str))

numpad[0][0] = "7"
numpad[1][0] = "8"
numpad[2][0] = "9"
numpad[0][1] = "4"
numpad[1][1] = "5"
numpad[2][1] = "6"
numpad[0][2] = "1"
numpad[1][2] = "2"
numpad[2][2] = "3"
numpad[0][3] = "#"
numpad[1][3] = "0"
numpad[2][3] = "A"

start_numpad = (2, 3)

keypad[0][0] = "#"
keypad[1][0] = "^"
keypad[2][0] = "A"
keypad[0][1] = "<"
keypad[1][1] = "v"
keypad[2][1] = ">"

start_keypad = (2, 0)

@functools.cache
def score(instruction):
    curr = ""
    count = 0

    for pos, char in enumerate(instruction):
        if char == curr:
            count += 1
        curr = char

    return count

@functools.cache
def favor_left(instruction):
    count = 0

    for pos, char in enumerate(instruction):
        if char == "<":
            count += len(instruction) - pos

    return count

@functools.cache
def favor_down(instruction):
    count = 0

    for pos, char in enumerate(instruction):
        if char == "v":
            count += len(instruction) - pos

    return count

@functools.cache
def distance(start, end):
    start_coord = (0, 0)
    end_coord = (0, 0)

    for x in keypad:
        for y in keypad[0]:
            if keypad[x][y] == start:
                start_coord = (x, y)

    for x in keypad:
        for y in keypad[0]:
            if keypad[x][y] == end:
                end_coord = (x, y)

    return abs(start_coord[0] - end_coord[0]) + abs(start_coord[1] - end_coord[1])

@functools.cache
def tie_break(instruction):
    count = 0
    curr = "A"

    for char in instruction:
        count += distance(curr, char)
        curr = char

    return 100000000 - count

def best_numpad(best_instructions):
    global start_numpad
    global start_keypad

    best_score = 0
    all_instructions = []
    potentials_instructions = []
    # Preparing to order second robot
    for instruction in best_instructions:
        command = instruction
        potentials_instructions.clear()
        
        # for command in current_instructions:
        for instruction in command:
            paths = keypad_search(start_keypad, instruction)
            potentials_instructions.append(directions_to_instructions(paths))
            start_keypad = paths[0][-1]
        
        # Building instructions from moves
        current_instructions = potentials_instructions[0]
        for i in range(1, len(potentials_instructions)):
            new_instructions = []
            for current_instruction in current_instructions:
                for instruction in potentials_instructions[i]:
                    new_instructions.append(current_instruction + instruction)
            current_instructions = new_instructions
        
        all_instructions = all_instructions + current_instructions

        for instruction in current_instructions:
            if tie_break(instruction) > best_score:
                best_score = tie_break(instruction)

    shortest = 10000000
    for instruction in all_instructions:
        if len(instruction) < shortest:
            shortest = len(instruction)

    shortest_instructions = set()
    for instruction in all_instructions:
        if len(instruction) == shortest:
            shortest_instructions.add(instruction)

    best_score = 0
    for instruction in shortest_instructions:
        if tie_break(instruction) > best_score:
            best_score = tie_break(instruction)

    best_instructions = set()
    for instruction in shortest_instructions:
        if tie_break(instruction) == best_score:
            best_instructions.add(instruction)

    any_instructions = []
    for instruction in best_instructions:
        any_instructions.append(instruction)
        break

    return any_instructions

def best_moves(command, robots):
    global start_numpad
    global start_keypad

    potentials_instructions = []

    for instruction in command:
        paths = breadth_first_search(numpad, valid_step, directions, start_numpad, instruction)
        potentials_instructions.append(directions_to_instructions(paths))
        start_numpad = paths[0][-1]

    current_instructions = potentials_instructions[0]
    for i in range(1, len(potentials_instructions)):
        new_instructions = []
        for current_instruction in current_instructions:
            for instruction in potentials_instructions[i]:
                new_instructions.append(current_instruction + instruction)
        current_instructions = new_instructions

    # best_score = 0
    # best_instruction = None
# 
    # best_tie_break = 0
# 
    # for instruction in current_instructions:
    #     if score(instruction) > best_score:
    #         best_score = score(instruction)
    #         best_instruction = instruction
    #         best_tie_break = tie_break(instruction)
    #     elif score(instruction) == best_score:
    #         breaker = tie_break(instruction)
    #         if breaker > best_tie_break:
    #             best_tie_break = breaker
    #             best_instruction = instruction

    best_score = 0
    
    for instruction in current_instructions:
        if tie_break(instruction) > best_score:
            best_score = tie_break(instruction)

    best_instructions = []
    for instruction in current_instructions:
        if tie_break(instruction) == best_score:
            best_instructions.append(instruction)

    # Correct

    # for instruction in current_instructions:
    #     if score(instruction) > best_score:
    #         best_score = score(instruction)
    #         best_instruction = instruction

    # print("best initial:", best_instructions)

    for _ in range(robots):
        best_instructions = best_numpad(best_instructions)
        # print(best_instructions)

    return best_instructions

def initial_moves(command):
    global start_numpad
    global start_keypad

    potentials_instructions = []

    for instruction in command:
        paths = breadth_first_search(numpad, valid_step, directions, start_numpad, instruction)
        potentials_instructions.append(directions_to_instructions(paths))
        start_numpad = paths[0][-1]

    current_instructions = potentials_instructions[0]
    for i in range(1, len(potentials_instructions)):
        new_instructions = []
        for current_instruction in current_instructions:
            for instruction in potentials_instructions[i]:
                new_instructions.append(current_instruction + instruction)
        current_instructions = new_instructions

    best_score = 0
    
    to_study = current_instructions
    best_instructions = []

    for instruction in to_study:
        if tie_break(instruction) > best_score:
            best_score = tie_break(instruction)

    for instruction in to_study:
        if tie_break(instruction) == best_score:
            best_instructions.append(instruction)

    best_score = 0

    to_study = copy.deepcopy(best_instructions)
    best_instructions.clear()

    for instruction in to_study:
        if score(instruction) > best_score:
            best_score = score(instruction)

    for instruction in to_study:
        if score(instruction) == best_score:
            best_instructions.append(instruction)

    best_score = 0

    to_study = copy.deepcopy(best_instructions)
    best_instructions.clear()

    for instruction in to_study:
        if favor_left(instruction) > best_score:
            best_score = favor_left(instruction)

    for instruction in to_study:
        if favor_left(instruction) == best_score:
            best_instructions.append(instruction)

    best_score = 0

    to_study = copy.deepcopy(best_instructions)
    best_instructions.clear()

    for instruction in to_study:
        if favor_down(instruction) > best_score:
            best_score = favor_down(instruction)

    for instruction in to_study:
        if favor_down(instruction) == best_score:
            best_instructions.append(instruction)

    

    return best_instructions

@functools.cache
def best_meta(start, target):
    starting_coordinates = (0, 0)

    for x in keypad:
        for y in keypad:
            if keypad[x][y] == start:
                starting_coordinates = (x, y)

    best_score = 0
    all_instructions = []
    potential_instructions = []
    current_instructions = []
    
    paths = keypad_search(starting_coordinates, target)
    potential_instructions.append(directions_to_instructions(paths))

    # Building instructions from moves
    current_instructions = potential_instructions[0]
    for i in range(1, len(potential_instructions)):
        new_instructions = []
        for current_instruction in current_instructions:
            for instruction in potential_instructions[i]:
                new_instructions.append(current_instruction + instruction)
        current_instructions = new_instructions
    
    all_instructions = all_instructions + current_instructions

    for instruction in current_instructions:
        if tie_break(instruction) > best_score:
            best_score = tie_break(instruction)

    shortest = 10000000
    for instruction in all_instructions:
        if len(instruction) < shortest:
            shortest = len(instruction)

    shortest_instructions = set()
    for instruction in all_instructions:
        if len(instruction) == shortest:
            shortest_instructions.add(instruction)

    best_score = 0
    for instruction in shortest_instructions:
        if tie_break(instruction) > best_score:
            best_score = tie_break(instruction)

    best_instructions = set()
    for instruction in shortest_instructions:
        if tie_break(instruction) == best_score:
            best_instructions.add(instruction)

    any_instruction = None
    for instruction in best_instructions:
        any_instruction = instruction
        break

    # print(best_instructions)

    return any_instruction

@functools.cache
def project(start, end, depth):
    moves = best_meta(start, end)
    # print(moves, depth)

    if depth == 1:
        return len(moves)
    
    sum = 0
    start = "A"
    for request in moves:
        sum += project(start, request, depth - 1)
        start = request
    
    return sum

def part1(input):
    commands = []

    for y, line in enumerate(input):
        line = line.replace('\n', '')
        if line != None:
            commands.append(line)

    sum = 0
    for command in commands:
        best_instructions = best_moves(command, 2)

        best = None
        for instruction in best_instructions:
            best = instruction
            break

        print(command, len(best))
        command = command.replace("A", "")
        sum += len(best) * int(command)

    # 126384: expected from example
    
    # 142222: too high
    # 141394: too high
    # 137870
    return sum

def part2(input):
    commands = []

    for line in input:
        line = line.replace('\n', '')
        if line != None:
            commands.append(line)
    
    # grid.display(keypad)

    # <^^^AvvvA^^Avv>A
    # print(project("A", "^", 2))

    sum = 0
    robots = 24

    for command in commands:
        # print("==============================")
        # print(command)
        moves = initial_moves(command)
        moves = moves[0]
        # print(moves)

        previous = "A"
        length = 0
        for move in moves:
            # print(previous, move, robots)
            length += project(previous, move, robots)
            previous = move

        # print(command, length)
        print(command, length)
        command = command.replace("A", "")
        sum += int(command) * length

    # sum = 0
    # robots = 2
    # for command in commands:
    #     previous = "A"
    #     moves = initial_moves(command)
# 
    #     # print(moves)
    #     moves = moves[0]
# 
    #     print("initial", moves)
# 
    #     for x in range(robots):
    #         print(x)
    #         buffer = []
# 
    #         for move in moves:
    #             buffer += best_meta(previous, move)
    #             previous = move
# 
    #         moves = buffer
    #         # print("".join(buffer))
    #         if x == robots - 1:
    #             command = command.replace("A", "")
    #             sum += len(moves) * int(command)

    
    # 91174183351724 : too low
    # 355699330596336: too high
    # 170279148659464
    return sum

if __name__ == "__main__":
    main()