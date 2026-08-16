import collections
import functools
import hashlib
import itertools
import math

from aoc import graph, grid, intcode, ints, letter, screen


TARGET = "input.txt"


def main():
    with open(TARGET, "r") as input_file:
        print(part1(input_file.readlines()))

    with open(TARGET, "r") as input_file:
        print(part2(input_file.readlines()))


class Moon:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.velocity = [0, 0, 0]

    def potential(self):
        return abs(self.position[0]) + abs(self.position[1]) + abs(self.position[2])

    def kinetic(self):
        return abs(self.velocity[0]) + abs(self.velocity[1]) + abs(self.velocity[2])

    def energy(self):
        return self.potential() * self.kinetic()

    def __hash__(self) -> int:
        # Is this shortcut going to work?
        return self.energy()

    def __repr__(self) -> str:
        return self.name

    def __str__(self) -> str:
        return f"position=<{self.position[0]:3d},{self.position[1]:3d},{self.position[2]:3d}>, velocity=<{self.velocity[0]:3d},{self.velocity[1]:3d},{self.velocity[2]:3d}>"


def part1(input):
    names = ["Io", "Europa", "Ganymede", "Callisto"]
    moons = []

    for index, line in enumerate(input):
        velocity = ints.extract(line.strip())

        moon = Moon(names[index], velocity)
        moons.append(moon)

    for _ in range(1000):
        for pair in itertools.combinations(moons, 2):
            left, right = pair

            for dimension in [0, 1, 2]:
                if left.position[dimension] < right.position[dimension]:
                    left.velocity[dimension] = left.velocity[dimension] + 1
                    right.velocity[dimension] = right.velocity[dimension] - 1
                elif left.position[dimension] > right.position[dimension]:
                    left.velocity[dimension] = left.velocity[dimension] - 1
                    right.velocity[dimension] = right.velocity[dimension] + 1

        for moon in moons:
            for dimension in [0, 1, 2]:
                moon.position[dimension] = (
                    moon.position[dimension] + moon.velocity[dimension]
                )

    system = 0
    for moon in moons:
        system = system + moon.energy()

    return system


def axis(moons, dimension):
    return tuple((moon.position[dimension], moon.velocity[dimension]) for moon in moons)


def part2(input):
    names = ["Io", "Europa", "Ganymede", "Callisto"]
    moons = []

    cycles = {"x": 0, "y": 0, "z": 0}

    for index, line in enumerate(input):
        velocity = ints.extract(line.strip())

        moon = Moon(names[index], velocity)
        moons.append(moon)

    initial = [axis(moons, dimension) for dimension in [0, 1, 2]]

    for iteration in itertools.count():
        for dimension, name in enumerate(cycles):
            if (
                iteration != 0
                and cycles[name] == 0
                and axis(moons, dimension) == initial[dimension]
            ):
                cycles[name] = iteration

        if all(cycles.values()):
            break

        for pair in itertools.combinations(moons, 2):
            left, right = pair

            for dimension in [0, 1, 2]:
                if left.position[dimension] < right.position[dimension]:
                    left.velocity[dimension] = left.velocity[dimension] + 1
                    right.velocity[dimension] = right.velocity[dimension] - 1
                elif left.position[dimension] > right.position[dimension]:
                    left.velocity[dimension] = left.velocity[dimension] - 1
                    right.velocity[dimension] = right.velocity[dimension] + 1

        for moon in moons:
            for dimension in [0, 1, 2]:
                moon.position[dimension] = (
                    moon.position[dimension] + moon.velocity[dimension]
                )

    return math.lcm(*cycles.values())


if __name__ == "__main__":
    main()
