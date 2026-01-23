import sys
sys.path.append("../../")

import collections
import functools
import graph
import letter
import hashlib
import re

def main():
    with open("input.txt", "r") as input_file:
        print(part1(input_file.readlines()))

    with open("input.txt", "r") as input_file:
        print(part2(input_file.readlines()))

before = collections.defaultdict(list)
after = collections.defaultdict(list)

printing_orders = []

def part1_sort(a, b):
    print(a,b)
    if b in before[a]:
        return -1
    elif a in before[b]:
        return 1
    
    return 0

part1_comp = functools.cmp_to_key(part1_sort)

def right_order(printing_order):
    for i in range(0, len(printing_order)):
        for j in range (i, len(printing_order)):
            if printing_order[j] in after[printing_order[i]]:
                return False, i, j

    # for value in printing_order:
    #     for second in printing_order:
    #         print(value, second)
    #         if value in before[second]:
    #             print("   ", before[value])
    #             return False
    return True, 0, 0

def swap(printing_order, i, j):
    new = printing_order[:]
    new[i], new[j] = printing_order[j], printing_order[i]
    return new

def part1(input):
    sum = 0

    ordering = True

    for line in input:
        line = line.replace('\n', '')
        if line != None:
            if line == "":
                ordering = False
                continue

            if ordering:
                left, right = map(int, line.split("|"))
                before[left].append(right)
                after[right].append(left)
            else:
                printing_orders.append(list(map(int, line.split(","))))

    for printing_order in printing_orders:
        ok, _, _ = right_order(printing_order)
        
        if ok:
            index = int((len(printing_order) - 1) / 2)
            sum += printing_order[index]

    return sum

def part2(input):
    sum = 0
    
    for printing_order in printing_orders:
        ok, i, j = right_order(printing_order)
        
        if not ok:
            while not ok:
                printing_order = swap(printing_order, i, j)
                ok, i, j = right_order(printing_order)

            index = int((len(printing_order) - 1) / 2)
            sum += printing_order[index]

    return sum

if __name__ == "__main__":
    main()