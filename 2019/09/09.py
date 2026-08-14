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


def part1(input):
    vm = intcode.IntCodeVM("part1")

    for line in input:
        line = line.strip()

        vm.input(1)
        vm.memory(ints.extract(line))
        for signal in vm.run():
            if signal == intcode.Signal.HCF:
                break

    return vm.outputs.pop()


def part2(input):
    vm = intcode.IntCodeVM("part2")

    for line in input:
        line = line.strip()

        vm.input(2)
        vm.memory(ints.extract(line))
        for signal in vm.run():
            if signal == intcode.Signal.HCF:
                break

    return vm.outputs.pop()


if __name__ == "__main__":
    main()
