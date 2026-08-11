import collections
import functools
import itertools
import hashlib
import math

from aoc import graph, grid, ints, letter, screen


TARGET = "input.txt"

DIRS: dict[str, tuple[int, int]] = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, 1),
    "D": (0, -1),
}


def walk(wire):
    path = set()
    location: tuple[int, int] = (0, 0)

    for move in wire:
        direction, distance = move[0], int(move[1:])
        change: tuple[int, int] = DIRS[direction]

        for _ in range(distance):
            location = grid.add(location, change)
            path.add(location)

    return path


def counting_walk(wire):
    path = set()
    steps_by_loc = {}
    steps = 0
    location: tuple[int, int] = (0, 0)

    for move in wire:
        direction, distance = move[0], int(move[1:])
        change: tuple[int, int] = DIRS[direction]

        for _ in range(distance):
            steps = steps + 1
            location = grid.add(location, change)
            path.add(location)
            if location not in steps_by_loc:
                steps_by_loc[location] = steps

    return path, steps_by_loc


def main():
    with open(TARGET, "r") as input_file:
        print(part1(input_file.readlines()))

    with open(TARGET, "r") as input_file:
        print(part2(input_file.readlines()))


def part1(input):
    smallest_distance = math.inf

    for index in range(0, len(input), 2):
        blue = input[index].strip().split(",")
        red = input[index + 1].strip().split(",")

        blue_path = walk(blue)
        red_path = walk(red)

        crossing_points = blue_path & red_path

        for point in crossing_points:
            distance = grid.manhattan(point)
            if distance < smallest_distance:
                smallest_distance = distance

    return smallest_distance


def part2(input):
    smallest_effort = math.inf

    for index in range(0, len(input), 2):
        blue = input[index].strip().split(",")
        red = input[index + 1].strip().split(",")

        blue_path, blue_sbl = counting_walk(blue)
        red_path, red_sbl = counting_walk(red)

        crossing_points = blue_path & red_path

        for point in crossing_points:
            effort = blue_sbl[point] + red_sbl[point]
            if effort < smallest_effort:
                smallest_effort = effort

    return smallest_effort


if __name__ == "__main__":
    main()
