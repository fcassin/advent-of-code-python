import collections
import hashlib
import json

from aoc import graph, ints, letter


def main():
    with open("input.txt", "r") as input_file:
        print(part1(input_file.readlines()))

    with open("input.txt", "r") as input_file:
        print(part2(input_file))

def part1(input):
    count = 0
    for line in input:
        if line != None:
            line = line.replace('\n', '')
            count = count + sum(ints.extract(line))

    return count
    
def unred(object):
    if isinstance(object, dict):
        if "red" in object.values():
            return 0
        else:
            return sum(unred(value) for value in object.values())
    elif isinstance(object, list):
        return sum(unred(item) for item in object)
    elif isinstance(object, int):
        return object
    else:
        return 0

def part2(input):
    parsed = json.load(input)
    return unred(parsed)

if __name__ == "__main__":
    main()
