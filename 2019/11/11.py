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


def robot(program, start=0):
    vm = intcode.IntCodeVM("robot")
    vm.memory(program)
    vm.input(start)

    # UP
    facing = 3
    space = grid.infinigrid()
    painted = set()
    position = (0, 0)
    painting = True

    while painting:
        for signal in vm.run():
            if signal == intcode.Signal.HCF:
                painting = False
                break
            elif signal == intcode.Signal.INP:
                color = vm.outputs.popleft()
                direction = vm.outputs.popleft()

                painted.add(position)
                if color == 0:
                    space[position[0]][position[1]] = "."
                else:
                    space[position[0]][position[1]] = "#"

                if direction == 0:
                    facing = (facing - 1) % 4
                else:
                    facing = (facing + 1) % 4

                position = grid.walk(position, grid.DIRS[facing])

                if space[position[0]][position[1]] == ".":
                    vm.input(0)
                else:
                    vm.input(1)

            else:
                raise Exception("unexpected signal")

    return painted, space


def part1(input):
    painted = set()

    for line in input:
        painted, space = robot(ints.extract(line.strip()))
        grid.display(grid.materialize(space))

    return len(painted)


def part2(input):
    plate = "????????"

    for line in input:
        painted, space = robot(ints.extract(line.strip()), 1)
        grid.display(grid.materialize(space))

        plate = screen.read_letters_from_grid(grid.materialize(space))

    return plate


if __name__ == "__main__":
    main()
