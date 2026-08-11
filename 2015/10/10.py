import collections
import hashlib

from aoc import graph


def main():
    with open("input.txt", "r") as input_file:
        print(part1(input_file.readlines()))

    with open("input.txt", "r") as input_file:
        print(part2(input_file.readlines()))

vertices = []
edges = []

def look_and_say(input):
    segment = []
    previous = "0"
    count = 0

    for char in input:
        if char != previous and previous == "0":
            previous = char
            count = count + 1
        elif char != previous:
            segment.append(str(count))
            segment.append(previous)
            previous = char
            count = 1
        else:
            count = count + 1

    segment.append(str(count))
    segment.append(previous)

    buffer = ""
    for char in segment:
        buffer = buffer + char

    return buffer

def part1(input):
    result = ""
    for line in input:
        if line != None:
            result = line

    for _ in range(40):
        result = look_and_say(result)
        
    return len(result)

def part2(input):
    result = ""
    for line in input:
        if line != None:
            result = line

    for _ in range(50):
        result = look_and_say(result)
        
    return len(result)

if __name__ == "__main__":
    main()
