import sys

sys.path.append("../../")

import collections
import enum
import functools
import graph
import grid
import ints
import itertools
import letter
import hashlib
import screen

TARGET = "input.txt"


# TODO: We will probably need to handle instruction length
class Op(enum.IntEnum):
    ADD = 1
    MUL = 2
    HCF = 99


def determine(mem):
    noun, verb = 0, 0

    for verb in range(100):
        for noun in range(100):
            work_mem = mem[:]
            work_mem[1] = noun
            work_mem[2] = verb
            work_mem = execute(work_mem)

            if work_mem[0] == 19690720:
                return noun, verb

    return 0, 0


def execute(mem: list[int]) -> list[int]:
    # instruction pointer
    ip = 0

    while True:
        match mem[ip]:
            case Op.ADD:
                mem[mem[ip + 3]] = mem[mem[ip + 1]] + mem[mem[ip + 2]]
            case Op.MUL:
                mem[mem[ip + 3]] = mem[mem[ip + 1]] * mem[mem[ip + 2]]
            case Op.HCF:
                return mem

        ip = ip + 4

    return mem


def main():
    with open(TARGET, "r") as input_file:
        print(part1(input_file.readlines()))

    with open(TARGET, "r") as input_file:
        print(part2(input_file.readlines()))


def part1(input):
    mem = []

    for line in input:
        line = line.strip()

        mem = [int(code) for code in line.split(",")]
        mem[1] = 12
        mem[2] = 2
        mem = execute(mem)

    return mem[0]


def part2(input):
    noun, verb = 0, 0
    mem = []

    for line in input:
        line = line.strip()

        mem = [int(code) for code in line.split(",")]
        noun, verb = determine(mem)
        print(noun, verb)

    return noun * 100 + verb


if __name__ == "__main__":
    main()
