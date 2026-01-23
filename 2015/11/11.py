import sys
sys.path.append("../../")

import collections
import graph
import letter
import hashlib

def main():
    with open("input.txt", "r") as input_file:
        print(part1(input_file.readlines()))

    with open("input.txt", "r") as input_file:
        print(part2(input_file.readlines()))

def is_valid(array):
    doubles = 0
    straight = 0

    forbidden_start = []

    for i in range(len(array)):
        if i < len(array) - 3:
            if array[i] == array[i + 1] - 1 == array[i + 2] - 2:
                straight = True

        if i < len(array) - 1:
            if array[i] == array[i + 1] and i not in forbidden_start:
                doubles = doubles + 1
                forbidden_start.append(i + 1)

        if array[i] in [8, 11, 14]:
            return False

    return straight >= 1 and doubles >= 2

def increment_char(char):
    new_char = (char + 1) % 26

    if new_char in [8, 11, 14]:
        new_char = new_char + 1

    return new_char, new_char == 0

def increment_password(array):
    pos = 8
    wrap = True

    while wrap == True:
        pos = pos - 1
        if pos < 0:
            wrap = False
        else:
            new_char, wrap = increment_char(array[pos])
            array[pos] = new_char

    return array

def next_password(password):
    if len(password) != 8:
        raise Exception("password length should be 8")
    
    array = [0 for _ in range(8)]
    for i, char in enumerate(password):
        array[i] = letter.atoi(char)

    valid = False
    while not valid:
        array = increment_password(array)
        valid = is_valid(array)

    buffer = ""
    for char in array:
        buffer = buffer + letter.itoa(char)

    return buffer

def part1(input):
    for line in input:
        if line != None:
            password = line
    
    return next_password(password)

def part2(input):
    for line in input:
        if line != None:
            password = line
    
    return next_password(next_password(password))

if __name__ == "__main__":
    main()