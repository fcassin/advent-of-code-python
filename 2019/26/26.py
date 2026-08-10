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
