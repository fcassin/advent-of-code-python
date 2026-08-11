import collections
import functools
import hashlib
import itertools
import math
from typing import DefaultDict

from aoc import graph, grid, intcode, ints, letter, screen


TARGET = "input.txt"


def main():
    with open(TARGET, "r") as input_file:
        print(part1(input_file.readlines()))

    with open(TARGET, "r") as input_file:
        print(part2(input_file.readlines()))


def part1(input):
    orbits = collections.defaultdict(list)

    for line in input:
        line = line.strip()

        orbited, orbiting = line.split(")")
        orbits[orbited].append(orbiting)

    total = 0
    indirect: collections.deque[tuple[str, int]] = collections.deque()
    indirect.append(("COM", 0))

    while len(indirect) > 0:
        current, count = indirect.popleft()

        for orbiting in orbits[current]:
            indirect.append((orbiting, count + 1))

        total = total + count

    return total


def part2(input):
    edges: dict[str, list[tuple[str, int]]] = dict()

    for line in input:
        line = line.strip()

        orbited, orbiting = line.split(")")

        if orbited not in edges:
            edges[orbited] = list()

        edges[orbited].append((orbiting, 1))

        if orbiting not in edges:
            edges[orbiting] = list()

        edges[orbiting].append((orbited, 1))

    return graph.breadth_first_search(edges, "YOU", "SAN") - 2


if __name__ == "__main__":
    main()
