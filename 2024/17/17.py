import collections
import copy
import functools
import itertools
import hashlib
import re

from aoc import graph, grid, letter


def main():
    with open("input.txt", "r") as input_file:
        lines = input_file.readlines()
        print(part1(lines))
        print(part2(lines))

originals = {
    "A": 0,
    "B": 0,
    "C": 0,
}

registers = {
    "A": 0,
    "B": 0,
    "C": 0,
}

def combo(value):
    if value in [0, 1, 2, 3]:
        return value
    elif value == 4:
        return registers["A"]
    elif value == 5:
        return registers["B"]
    elif value == 6:
        return registers["C"]
    elif value == 7:
        assert False, "7 should not appear as a combo value"
    else:
        # print("combo", value)
        assert False, "unknown value"

def adv(operand):
    num = registers["A"]
    denom = 2 ** combo(operand)

    result = num // denom
    registers["A"] = result
    return result

def bxl(operand):
    result = registers["B"] ^ operand
    registers["B"] = result
    return result

def bst(operand):
    result = combo(operand) % 8
    registers["B"] = result
    return result

def jnz(operand):
    a_val = registers["A"]
    if a_val == 0:
        return -1
    inst_pointer = operand
    return inst_pointer

def bxc(operand):
    result = registers["B"] ^ registers["C"]
    registers["B"] = result
    return result

def out(operand):
    result = combo(operand) % 8
    return result

def bdv(operand):
    num = registers["A"]
    denom = 2 ** combo(operand)

    result = num // denom
    registers["B"] = result
    return result

def cdv(operand):
    num = registers["A"]
    denom = 2 ** combo(operand)

    result = num // denom
    registers["C"] = result
    return result

def compute(ivs):
    outputs = []
    inst_pointer = 0
    length = len(ivs)

    while True:
        if inst_pointer % 2 == 1:
            print("odd inst_pointer")

        if inst_pointer >= length:
            break

        instruction = ivs[inst_pointer]
        operand = ivs[inst_pointer + 1]

        # if len(outputs) > length:
        #     break

        if instruction == 0:
            adv(operand)
            inst_pointer += 2
            continue
        elif instruction == 1:
            bxl(operand)
            inst_pointer += 2
            continue
        elif instruction == 2:
            bst(operand)
            inst_pointer += 2
            continue
        elif instruction == 3:
            result = jnz(operand)
            if result == -1:
                inst_pointer += 2
            else:
                inst_pointer = result
            continue
        elif instruction == 4:
            bxc(operand)
            inst_pointer += 2
            continue
        elif instruction == 5:
            outputs.append(out(operand))
            inst_pointer += 2
            continue
        elif instruction == 6:
            bdv(operand)
            inst_pointer += 2
            continue
        elif instruction == 7:
            cdv(operand)
            inst_pointer += 2
            continue

    return ",".join([str(x) for x in outputs])

def part1(input):
    count = 0

    reading_registers = True
    for y, line in enumerate(input):
        line = line.replace('\n', '')
        if line != None:
            if line == "":
                reading_registers = False
                continue

            if reading_registers:
                r, v = line.split(":")
                r = r.split(" ")[1]
                v = int(v)
                registers[r] = v
            else:
                ivs = [int(x) for x in line.split(":")[1].split(",")]

    return compute(ivs)

def find(program, ans):
    global attempts
    if program == []:
        return ans
    for mb in range(8):
        a = ans << 3 | mb
        # 2,4,1,1,7,5,1,5,0,3,4,3,5,5,3,0
        b = a % 8
        b = b ^ 1
        c = a >> b
        b = b ^ 5
        # a = a >> 3
        b = b ^ c
        if b % 8 == program[-1]:
            sub = find(program[:-1], a)
            if sub is None:
                continue
            return sub

def part2(input):
    count = 0

    reading_registers = True
    for y, line in enumerate(input):
        line = line.replace('\n', '')
        if line != None:
            if line == "":
                reading_registers = False
                continue

            if reading_registers:
                r, v = line.split(":")
                r = r.split(" ")[1]
                v = int(v)
                registers[r] = v
                originals[r] = v
            else:
                program = line.split(":")[1].split()[0]
                ivs = [int(x) for x in line.split(":")[1].split(",")]

    result = find(ivs, 0)

    return result

if __name__ == "__main__":
    main()
