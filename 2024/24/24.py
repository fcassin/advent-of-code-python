import collections
import copy
import functools
import itertools
import hashlib
import re

from aoc import graph, grid, letter


map = collections.defaultdict(lambda: collections.defaultdict(str))

def main():
    with open("input.txt", "r") as input_file:
        lines = input_file.readlines()
        print(part1(lines))
        print(part2(lines))

inputs = {}
gates = collections.deque([])

def part1(input):
    parsingInputs = True

    for line in input:
        line = line.replace('\n', '')
        if line != None:
            if line == "":
                parsingInputs = False
                continue

            if parsingInputs:
                wire, value = line.split(": ")
                value = int(value)
                inputs[wire] = value
            else:
                gate, output = line.split(" -> ")
                if " AND " in gate:
                    op = "AND"
                    left, right = gate.split(" AND ")
                if " XOR " in gate:
                    op = "XOR"
                    left, right = gate.split(" XOR ")
                if " OR " in gate:
                    op = "OR"
                    left, right = gate.split(" OR ")

                gates.append((left, op, right, output))

    while len(gates) > 0:
        gate = gates.popleft()
        left, op, right, output = gate

        if left in inputs and right in inputs:
            if op == "AND":
                inputs[output] = inputs[left] & inputs[right]
            elif op == "OR":
                inputs[output] = inputs[left] | inputs[right]
            elif op == "XOR":
                inputs[output] = inputs[left] ^ inputs[right]
        else:
            gates.append(gate)

    bool_value = 0
    for wire, value in inputs.items():
        if wire.startswith('z'):
            offset = int(wire.replace('z', ''))
            bool_value = bool_value + (value << offset)

    return bool_value



def study_wrong(computed, size):
    wrong_zs = []

    carry = 0
    xVals = [0 for i in range(size)]
    yVals = [0 for i in range(size)]
    zVals = [0 for i in range(size)]
    for counter in range(size):
        xBit = f"x{counter:02}"
        yBit = f"y{counter:02}"
        zBit = f"z{counter:02}"
        
        xVals[counter] = str(computed[xBit])
        yVals[counter] = str(computed[yBit])
        zVals[counter] = str(computed[zBit])

        expected = computed[xBit] + computed[yBit] + carry
        if expected >= 2:
            expected = expected % 2
            carry = 1
        else:
            carry = 0

        if computed[zBit] != expected:
            print(xBit, computed[xBit], yBit, computed[yBit], zBit, computed[zBit], "wrong")
            wrong_zs.append(counter)
        else:
            print(xBit, computed[xBit], yBit, computed[yBit], zBit, computed[zBit], "right")

    # print("".join(reversed(xVals)))
    # print("".join(reversed(yVals)))
    # print("".join(reversed(zVals)))

    return wrong_zs

upstream = collections.defaultdict(list)

def buildUpstream(wire):
    direct = [up for up in upstream[wire]]

    for d in direct:
        # print("direct", d)
        # print("direct0", d[0])
        # print("direct2", d[2])
        if (d[0].startswith('x') or d[0].startswith('y')) and (d[2].startswith('x') or d[2].startswith('y')):
            return [d]
    
        return direct + buildUpstream(d[0]) + buildUpstream(d[2])

def compute(inputs, gates):
    while len(gates) > 0:
        gate = gates.popleft()
        left, op, right, output = gate

        if left in inputs and right in inputs:
            if op == "AND":
                inputs[output] = inputs[left] & inputs[right]
            elif op == "OR":
                inputs[output] = inputs[left] | inputs[right]
            elif op == "XOR":
                inputs[output] = inputs[left] ^ inputs[right]
        else:
            gates.append(gate)
    return inputs

def part2(input):
    inputs.clear()
    parsingInputs = True

    for line in input:
        line = line.replace('\n', '')
        if line != None:
            if line == "":
                parsingInputs = False
                continue

            if parsingInputs:
                wire, value = line.split(": ")
                value = int(value)
                inputs[wire] = value
            else:
                gate, output = line.split(" -> ")
                if " AND " in gate:
                    op = "AND"
                    left, right = gate.split(" AND ")
                if " XOR " in gate:
                    op = "XOR"
                    left, right = gate.split(" XOR ")
                if " OR " in gate:
                    op = "OR"
                    left, right = gate.split(" OR ")

                gates.append((left, op, right, output))
                upstream[output].append((left, op, right))


    # Part 2
    """ size = 45

    original_inputs = dict(inputs)
    original_gates = collections.deque(gates)

    computed = compute(original_inputs, original_gates)

    wrong_zs = study_wrong(computed, size)
    
    # print(wrong_zs)

    most_wrong = collections.defaultdict(int)

    for count in range(size):
        if count in wrong_zs:
            up = buildUpstream(f'z{count:02}')
            # print()
            # print(f'z{count:02}', upstream[f'z{count:02}'], set(up))

            for u in set(up):
                most_wrong[u] += 1

    print(most_wrong) """

    # qff, qnw, qqp, z23, z36, fbq, pbv, z16
    # fbq,pbv,qff,qnw,qqp,z16,z23,z36

    return "fbq,pbv,qff,qnw,qqp,z16,z23,z36"

if __name__ == "__main__":
    main()
