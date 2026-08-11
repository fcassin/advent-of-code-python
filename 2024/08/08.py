import collections
import functools
import itertools
import hashlib
import re

from aoc import graph, grid, letter


def main():
    with open("input.txt", "r") as input_file:
        print(part1(input_file.readlines()))

    with open("input.txt", "r") as input_file:
        print(part2(input_file.readlines()))

map = collections.defaultdict(lambda:collections.defaultdict(str))

def part1(input):
    count = 0

    nodes = collections.defaultdict(list)

    for y, line in enumerate(input):
        line = line.replace('\n', '')
        if line != None:
            for x, char in enumerate(line):
                map[x][y] = char
                if char != ".":
                    nodes[char].append((x, y))

    grid.display(map)
    # print(nodes)

    seen = set()
    antinodes = set()
    width = len(map)
    height = len(map)

    for char, positions in nodes.items():
        # print(char, positions)
        for left, right in itertools.permutations(positions, 2):
            if (right, left) not in seen:
                seen.add((left, right))

                vector_x = left[0] - right[0]
                vector_y = left[1] - right[1]
                vector = (vector_x, vector_y)
                
                antinode_a = (left[0] + vector[0], left[1] + vector[1])
                antinode_b = (right[0] - vector[0], right[1] - vector[1])
                
                if antinode_a[0] >= 0 and antinode_a[0] < width and antinode_a[1] >= 0 and antinode_a[1] < height:
                    # print(left, right, " - ", vector, ":", antinode_a)
                    # map[antinode_a[0]][antinode_a[1]] = "#"
                    antinodes.add(antinode_a)

                if antinode_b[0] >= 0 and antinode_b[0] < width and antinode_b[1] >= 0 and antinode_b[1] < height:
                    # print(left, right, " - ", vector, ":", antinode_b)
                    # map[antinode_b[0]][antinode_b[1]] = "#"
                    antinodes.add(antinode_b)

    # grid.display(map)

    return len(antinodes)

def part2(input):
    count = 0

    nodes = collections.defaultdict(list)

    for y, line in enumerate(input):
        line = line.replace('\n', '')
        if line != None:
            for x, char in enumerate(line):
                map[x][y] = char
                if char != ".":
                    nodes[char].append((x, y))

    grid.display(map)
    print(nodes)

    seen = set()
    antinodes = set()
    width = len(map)
    height = len(map)

    for char, positions in nodes.items():
        print(char, positions)
        for left, right in itertools.permutations(positions, 2):
            if (right, left) not in seen:
                seen.add((left, right))

                vector_x = left[0] - right[0]
                vector_y = left[1] - right[1]
                vector = (vector_x, vector_y)
                
                current_antinode_a = left
                while current_antinode_a[0] >= 0 and current_antinode_a[0] < width and current_antinode_a[1] >= 0 and current_antinode_a[1] < height:
                    antinodes.add(current_antinode_a)

                    current_antinode_a = (current_antinode_a[0] + vector[0], current_antinode_a[1] + vector[1])

                current_antinode_b = right
                while current_antinode_b[0] >= 0 and current_antinode_b[0] < width and current_antinode_b[1] >= 0 and current_antinode_b[1] < height:
                    antinodes.add(current_antinode_b)

                    current_antinode_b = (current_antinode_b[0] - vector[0], current_antinode_b[1] - vector[1])

    grid.display(map)

    return len(antinodes)

if __name__ == "__main__":
    main()
