import collections
import functools
import hashlib
import itertools
import math

from aoc import graph, grid, ints, letter, screen


INPUT = "382345-843167"


def valid(value):
    pairs = list(itertools.pairwise(str(value)))
    return all(a <= b for a, b in pairs) and any(a == b for a, b in pairs)


def valid_strict(value):
    pairs = list(itertools.pairwise(str(value)))

    if not all(a <= b for a, b in pairs):
        return False

    if not any(a == b for a, b in pairs):
        return False

    runs = [len(list(groups)) for _, groups in itertools.groupby(str(value))]
    if 2 not in runs:
        return False

    return True


def main():
    print(part1(INPUT))
    print(part2(INPUT))


def part1(input):
    lo, hi = [int(value) for value in input.split("-")]
    return sum(map(valid, range(lo, hi + 1)))


def part2(input):
    lo, hi = [int(value) for value in input.split("-")]
    return sum(map(valid_strict, range(lo, hi + 1)))


if __name__ == "__main__":
    main()
