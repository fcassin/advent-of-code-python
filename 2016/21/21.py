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

def index_of(chars, a):
    for i in range(len(chars)):
        if chars[i] == a:
            return i
    
def swap_positions(chars, x, y):
    chars[x], chars[y] = chars[y], chars[x]
    return chars

def swap_letters(chars, a, b):
    x = index_of(chars, a)
    y = index_of(chars, b)
    return swap_positions(chars, x, y)

def rotate(chars, steps):
    steps = steps % len(chars)
    return chars[-steps:] + chars[:-steps]

def rotate_based_on_position(chars, a):
    index = index_of(chars, a)
    steps = 1 + index
    if index >= 4:
        steps += 1
    return rotate(chars, steps)

def reverse_based_on_position(chars, a):
    length = len(chars)
    for i in range(length):
        test_chars = rotate(chars, -i)
        if rotate_based_on_position(test_chars, a) == chars:
            return test_chars

def reverse_positions(chars, x, y):
    chars[x:y+1] = reversed(chars[x:y+1])
    return chars

def move_position(chars, x, y):
    letter = chars[x]
    if x < y:
        for i in range(x, y):
            chars[i] = chars[i+1]
    else:
        for i in range(x, y, -1):
            chars[i] = chars[i-1]
    chars[y] = letter
    return chars    
    
def part1(input):
    chars = list("abcdefgh")
    
    for line in input:
        line = line.strip()
        
        if line.startswith("swap position"):
            parts = line.split(" ")
            x = int(parts[2])
            y = int(parts[5])
            chars = swap_positions(chars, x, y)
        elif line.startswith("swap letter"):
            parts = line.split(" ")
            a = parts[2]
            b = parts[5]
            chars = swap_letters(chars, a, b)
        elif line.startswith("rotate left"):
            parts = line.split(" ")
            steps = int(parts[2])
            chars = rotate(chars, -steps)
        elif line.startswith("rotate right"):
            parts = line.split(" ")
            steps = int(parts[2])
            chars = rotate(chars, steps)
        elif line.startswith("rotate based on"):
            parts = line.split(" ")
            a = parts[6]
            chars = rotate_based_on_position(chars, a)
        elif line.startswith("reverse positions"):
            parts = line.split(" ")
            x = int(parts[2])
            y = int(parts[4])
            chars = reverse_positions(chars, x, y)
        elif line.startswith("move position"):
            parts = line.split(" ")
            x = int(parts[2])
            y = int(parts[5])
            chars = move_position(chars, x, y)
        
    return "".join(chars)

def part2(input):
    chars = list("fbgdceah")
    
    for line in reversed(input):
        line = line.strip()
        
        if line.startswith("swap position"):
            parts = line.split(" ")
            x = int(parts[2])
            y = int(parts[5])
            chars = swap_positions(chars, x, y)
        elif line.startswith("swap letter"):
            parts = line.split(" ")
            a = parts[2]
            b = parts[5]
            chars = swap_letters(chars, a, b)
        elif line.startswith("rotate left"):
            parts = line.split(" ")
            steps = int(parts[2])
            chars = rotate(chars, steps)
        elif line.startswith("rotate right"):
            parts = line.split(" ")
            steps = int(parts[2])
            chars = rotate(chars, -steps)
        elif line.startswith("rotate based on"):
            parts = line.split(" ")
            a = parts[6]
            chars = reverse_based_on_position(chars, a)
            # Inverse rotation based on position
            # length = len(chars)
            # for i in range(length):
            #     test_chars = rotate(chars, -i)
            #     if rotate_based_on_position(test_chars, a) == chars:
            #         chars = test_chars
            #         break
        elif line.startswith("reverse positions"):
            parts = line.split(" ")
            x = int(parts[2])
            y = int(parts[4])
            chars = reverse_positions(chars, x, y)
        elif line.startswith("move position"):
            parts = line.split(" ")
            x = int(parts[2])
            y = int(parts[5])
            chars = move_position(chars, y, x)
            
    return "".join(chars)

if __name__ == "__main__":
    main()