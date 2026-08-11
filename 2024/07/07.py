import collections
import functools
import itertools
import hashlib
import re

from aoc import graph, letter


def main():
    with open("input.txt", "r") as input_file:
        print(part1(input_file.readlines()))

    with open("input.txt", "r") as input_file:
        print(part2(input_file.readlines()))

def evaluate(test, remaining):
    length = len(remaining)

    for _, perm in enumerate(itertools.product('+*', repeat=length-1)):
        result = 0

        for i, operator in enumerate(perm):
            if result == 0:
                result = remaining[0]

            if operator == "+":
                result = result + remaining[i+1]
            elif operator == "*":
                result = result * remaining[i+1]

            if result > test:
                break

        if result == test:
            return 1

    return 0

def evaluate_concat(test, remaining):
    length = len(remaining)
    
    for _, perm in enumerate(itertools.product('+*|', repeat=length-1)):

        result = 0

        for i, operator in enumerate(perm):
            if result == 0:
                result = remaining[0]

            if operator == "+":
                result = result + remaining[i+1]
            elif operator == "*":
                result = result * remaining[i+1]
            elif operator == "|":
                result = int(str(result) + str(remaining[i+1]))

            if result > test:
                break

        if result == test:
            return 1

    return 0

def part1(input):
    sum = 0

    for line in input:
        line = line.replace('\n', '')
        if line != None:
            test, remaining = line.split(':')
            test = int(test)
            remaining = list(map(int, remaining.split()))
            print(line, " - ", test, remaining)
            if evaluate(test, remaining):
                sum += test

    return sum

def part2(input):
    sum = 0

    for line in input:
        line = line.replace('\n', '')
        if line != None:
            test, remaining = line.split(':')
            test = int(test)
            remaining = list(map(int, remaining.split()))
            print(line, " - ", test, remaining)
            if evaluate_concat(test, remaining):
                sum += test

    return sum

if __name__ == "__main__":
    main()
