import collections
import functools
import hashlib
import itertools
import math

from aoc import graph, grid, intcode, ints, letter, screen


TARGET = "input.txt"


def main():
    with open(TARGET, "r") as input_file:
        print(part1(input_file.readlines()))

    with open(TARGET, "r") as input_file:
        print(part2(input_file.readlines()))


def part1(input):
    for line in input:
        line = line.strip()

        print(line)

    return 0


def part2(input):
    return 0


if __name__ == "__main__":
    main()
