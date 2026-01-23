import sys
sys.path.append("../../")

import collections
import functools
import graph
import ints
import itertools
import letter
import hashlib

def main():
    with open("input.txt", "r") as input_file:
        print(part1(input_file.readlines()))

    with open("input.txt", "r") as input_file:
        print(part2(input_file.readlines()))

numpad = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

directions = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1),
}

def move(position, direction):
    delta = directions[direction]
    new_position = (position[0] + delta[0], position[1] + delta[1])
    if 0 <= new_position[0] < 3 and 0 <= new_position[1] < 3:
        return new_position
    return position

def part1(input):
    code = []
    position = (1, 1)
    
    for line in input:
        for char in line.strip():
            position = move(position, char)
        code.append(numpad[position[0]][position[1]])
        
    return ''.join(map(str, code))

actual_numpad = [
    [None, None, 1, None, None],
    [None, 2, 3, 4, None],
    [5, 6, 7, 8, 9],
    [None, 'A', 'B', 'C', None],
    [None, None, 'D', None, None]
]

def move_actual(position, direction):
    delta = directions[direction]
    new_position = (position[0] + delta[0], position[1] + delta[1])
    if 0 <= new_position[0] < 5 and 0 <= new_position[1] < 5 and actual_numpad[new_position[0]][new_position[1]] is not None:
        return new_position
    return position

def part2(input):
    code = []
    position = (2, 0)
    
    for line in input:
        for char in line.strip():
            position = move_actual(position, char)
        code.append(actual_numpad[position[0]][position[1]])
        
    return ''.join(map(str, code))

if __name__ == "__main__":
    main()