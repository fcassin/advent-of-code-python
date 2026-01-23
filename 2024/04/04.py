import sys
sys.path.append("../../")

import collections
import graph
import letter
import hashlib
import re

def main():
    with open("input.txt", "r") as input_file:
        print(part1(input_file.readlines()))

    with open("input.txt", "r") as input_file:
        print(part2(input_file.readlines()))

def search(crosswords, x, y):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    count = 0
    if crosswords[x][y] == "X":
        for direction in directions:
            if crosswords[x + direction[0]][y + direction[1]] == "M":
                if crosswords[x + 2*direction[0]][y + 2*direction[1]] == "A":
                    if crosswords[x + 3*direction[0]][y + 3*direction[1]] == "S":
                        count += 1

    return count

def x_search(crosswords, x, y):
    top_left = (-1, -1)
    top_right = (1, -1)
    bottom_left = (-1, 1)
    bottom_right = (1, 1)

    found = 0
    if crosswords[x][y] == "A":
        if crosswords[x + top_left[0]][y + top_left[1]] == "M" and crosswords[x + bottom_right[0]][y + bottom_right[1]] == "S":
            found += 1
        elif crosswords[x + top_left[0]][y + top_left[1]] == "S" and crosswords[x + bottom_right[0]][y + bottom_right[1]] == "M":
            found += 1

        if crosswords[x + top_right[0]][y + top_right[1]] == "M" and crosswords[x + bottom_left[0]][y + bottom_left[1]] == "S":
            found += 1
        elif crosswords[x + top_right[0]][y + top_right[1]] == "S" and crosswords[x + bottom_left[0]][y + bottom_left[1]] == "M":
            found += 1

        if found == 2:
            return 1

    return 0


def part1(input):
    sum = 0

    crossword = collections.defaultdict(lambda: collections.defaultdict(str))

    min = -3
    max = len(input) + 3

    for x in range(min,max):
        for y in range(min,max):
            crossword[x][y] == "Z"

    for y, line in enumerate(input):
        line = line.replace('\n', '')
        if line != None:
            for x, char in enumerate(line):
                crossword[x][y] = char

    for x in crossword:
        for y in crossword[x]:
            sum += search(crossword, x, y)

    return sum

def part2(input):
    sum = 0

    crossword = collections.defaultdict(lambda: collections.defaultdict(str))

    min = -1
    max = len(input) + 1

    for x in range(min,max):
        for y in range(min,max):
            crossword[x][y] == "Z"

    for y, line in enumerate(input):
        line = line.replace('\n', '')
        if line != None:
            
            for x, char in enumerate(line):
                crossword[x][y] = char

    for x in crossword:
        for y in crossword[x]:
            sum += x_search(crossword, x, y)

    return sum

if __name__ == "__main__":
    main()