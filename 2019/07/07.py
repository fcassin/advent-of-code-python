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


def loop(permutations, memories, init):
    results = dict()
    layouts = dict()

    best = ([], 0)
    layout = [[], [], [], [], []]

    for permutation in itertools.permutations(permutations):
        previous = init
        programs = [[], [], [], [], []]
        output = [0]

        for index, phase in enumerate(permutation):
            mem = memories[index][:]

            mem, output = intcode.execute(mem, [phase, previous])
            previous = output[0]
            programs[index] = mem

        results[permutation] = output[0]
        layouts[permutation] = programs

    for key, value in results.items():
        if value > best[1]:
            best = (key, value)
            layout = layouts[key]

    return best[0], best[1], layout


def combination(input):
    value = 0

    for line in input:
        memories = [[], [], [], [], []]
        for index in range(5):
            memories[index] = ints.extract(line)[:]

        permutation, value, layouts = loop([0, 1, 2, 3, 4], memories, 0)

    return value


def part1(input):
    return combination(input)


def part2_loop(program, permutations):
    a = intcode.IntCodeVM("A")
    b = intcode.IntCodeVM("B")
    c = intcode.IntCodeVM("C")
    d = intcode.IntCodeVM("D")
    e = intcode.IntCodeVM("E")

    vms = [a, b, c, d, e]

    for index, permutation in enumerate(permutations):
        vms[index].memory(ints.extract(program))
        vms[index].input(permutation)

    a.input(0)

    current = 0
    while True:
        for signal in vms[current].run():
            next = (current + 1) % 5
            match signal:
                case intcode.Signal.EOT:
                    raise Exception("unexpected end of tape")
                case intcode.Signal.HCF:
                    if current == 4:
                        return vms[current].outputs.pop()
                    else:
                        output = vms[current].outputs.pop()
                        vms[next].input(output)
                        current = next
                        break

                case intcode.Signal.INP:
                    output = vms[current].outputs.pop()
                    vms[next].input(output)
                    current = next
                    break

    return 0


def part2(input):
    best = 0
    perm = []

    for line in input:
        for permutation in itertools.permutations(range(5, 10)):
            result = part2_loop(line, permutation)
            if result > best:
                best = result
                perm = permutation

    print(f"best result: {best}\nfor permutation: {perm}")

    return best


if __name__ == "__main__":
    main()
