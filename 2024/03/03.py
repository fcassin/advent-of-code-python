import collections
import hashlib
import re

from aoc import graph, letter


def main():
    with open("input.txt", "r") as input_file:
        print(part1(input_file.readlines()))

    with open("input.txt", "r") as input_file:
        print(part2(input_file.readlines()))

def part1(input):
    sum = 0
    for line in input:
        line = line.replace('\n', '')
        if line != None:
            for pattern in re.findall('mul\\(\\d*,\\d*\\)', line):
                pattern = pattern.replace('mul(', '')
                pattern = pattern.replace(')', '')
                pattern = pattern.replace(',', ' ')
                left, right = pattern.split()
                sum += int(left) * int(right)

    return sum

def part2(input):
    sum = 0
    enabled = True

    for line in input:
        line = line.replace('\n', '')
        if line != None:
            for pattern in re.findall('mul\\(\\d*,\\d*\\)|do\(\)|don\'t\(\)', line):
                if pattern == "do()":
                    enabled = True
                    continue
                elif pattern == "don't()":
                    enabled = False
                    continue
                elif enabled:
                    pattern = pattern.replace('mul(', '')
                    pattern = pattern.replace(')', '')
                    pattern = pattern.replace(',', ' ')
                    left, right = pattern.split()
                    sum += int(left) * int(right)

    return sum

if __name__ == "__main__":
    main()
