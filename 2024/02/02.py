import collections
import hashlib

from aoc import graph, letter


def main():
    with open("input.txt", "r") as input_file:
        print(part1(input_file.readlines()))

    with open("input.txt", "r") as input_file:
        print(part2(input_file.readlines()))

def increasing(report):
    current_level = 0
    errors = 0

    for level in report:
        level = int(level)
        if current_level == 0:
            current_level = level
            continue

        diff = abs(level - current_level)

        if level < current_level or diff > 3 or diff == 0:
            errors += 1
        
        current_level = level

    return errors

def decreasing(report):
    current_level = 0
    errors = 0

    for level in report:
        level = int(level)
        if current_level == 0:
            current_level = level
            continue

        diff = abs(level - current_level)

        if level > current_level or diff > 3 or diff == 0:
            errors += 1
        
        current_level = level

    return errors

def safe(report):
    if increasing(report) ==0 or decreasing(report) == 0:
        return True
    return False

def dampener(report):
    i = increasing(report)
    d = decreasing(report)

    if i == 0 or d == 0:
        return True

    if i >= 1:
        for pos, _ in enumerate(report):
            copy = report[:]
            copy.pop(pos)
            
            if increasing(copy) == 0:
                return True

    if d >= 1:
        for pos, _ in enumerate(report):
            copy = report[:]
            copy.pop(pos)
            
            if decreasing(copy) == 0:
                return True    

    return False

def part1(input):
    count = 0
    for line in input:
        if line != None:
            if safe(line.split()):
                count += 1    

    return count

def part2(input):
    count = 0
    for line in input:
        if line != None:
            if dampener(line.split()):
                count += 1    

    return count

if __name__ == "__main__":
    main()
