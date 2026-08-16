import collections
import functools
import hashlib
import itertools
import math

from aoc import graph, grid, intcode, ints, letter, screen


TARGET = "input.txt"
MONITORING_STATION = (0, 0)


def main():
    with open(TARGET, "r") as input_file:
        print(part1(input_file.readlines()))

    with open(TARGET, "r") as input_file:
        print(part2(input_file.readlines()))


def part1(input):
    global MONITORING_STATION

    space = grid.parse(input)
    # grid.display(space)

    asteroids = []
    width = len(space)
    height = len(space[0])
    for x in range(width):
        for y in range(height):
            if space[x][y] == "#":
                asteroids.append((x, y))

    best = ((0, 0), 0)
    for asteroid in asteroids:
        lines = []
        for match in asteroids:
            if asteroid != match:
                lines.append((asteroid, match))

        lines.sort(key=lambda x: math.dist(x[0], x[1]))

        visible = 0
        obscured = set()
        for line in lines:
            origin, dest = line
            slope = (dest[0] - origin[0], dest[1] - origin[1])

            gcd = math.gcd(slope[0], slope[1])
            slope = (slope[0] // gcd, slope[1] // gcd)

            x, y = dest
            x = x + slope[0]
            y = y + slope[1]
            while 0 <= x < width and 0 <= y < height:
                obscured.add((x, y))

                x = x + slope[0]
                y = y + slope[1]

            if dest not in obscured:
                visible = visible + 1

        if visible > best[1]:
            best = (asteroid, visible)

    MONITORING_STATION = best[0]

    return best[1]


def part2(input):
    space = grid.parse(input)

    asteroids = []
    width = len(space)
    height = len(space[0])
    for x in range(width):
        for y in range(height):
            if space[x][y] == "#":
                asteroids.append((x, y))

    asteroids_by_vector = collections.defaultdict(list)
    lines = []
    for asteroid in asteroids:
        lines.append((MONITORING_STATION, asteroid))

    for line in lines:
        origin, dest = line
        if origin != dest:
            slope = (dest[0] - origin[0], dest[1] - origin[1])
            gcd = math.gcd(slope[0], slope[1])
            slope = (slope[0] // gcd, slope[1] // gcd)

            asteroids_by_vector[slope].append(dest)

    # print(asteroids_by_vector)
    ordered = []
    for key, val in asteroids_by_vector.items():
        ordered.append((key, val))

    ordered.sort(key=lambda x: (math.atan2(x[0][0], -x[0][1])) % (2 * math.pi))
    for val in ordered:
        val[1].sort(key=lambda x: math.dist(MONITORING_STATION, x))

    destroyed = []
    iteration = 0
    while len(destroyed) < len(asteroids) - 1:
        for cluster in ordered:
            if len(cluster[1]) > iteration:
                destroyed.append(cluster[1][iteration])

        iteration = iteration + 1

    return destroyed[199][0] * 100 + destroyed[199][1]


if __name__ == "__main__":
    main()
