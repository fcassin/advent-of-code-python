import sys
sys.path.append("../../")

import collections
import functools
import graph
import grid
import ints
import itertools
import letter
import hashlib
import screen

def main():
    with open("input.txt", "r") as input_file:
        print(part1(input_file.readlines()))

    with open("input.txt", "r") as input_file:
        print(part2(input_file.readlines()))
    
def part1(input):
    elfs = 3018458
    gifts_per_elf = {}
    
    for i in range(1, elfs + 1):
        gifts_per_elf[i] = 1
    
    current_elf = 1
    while True:
        if current_elf not in gifts_per_elf:
            current_elf = (current_elf + 1) % elfs
            continue
        
        if len(gifts_per_elf) == 1:
            break
        
        next_elf = current_elf + 1 % elfs
        while next_elf not in gifts_per_elf:
            next_elf = (next_elf + 1) % elfs
        
        gifts_per_elf[current_elf] += gifts_per_elf.get(next_elf)
        gifts_per_elf.pop(next_elf)
        
        current_elf = (current_elf + 1) % elfs
        
        print(len(gifts_per_elf))
        
    return list(gifts_per_elf.keys())[0]

def solve_circle(n):
    elves = collections.deque(range(0, n))
    
    current_elf = 0
    while len(elves) > 1:
        length = len(elves)
        target = (current_elf + length // 2) % length
        
        elf = elves[current_elf]
        
        # print("Current elf:", elves[current_elf] + 1, "target:", target)
        # print(elves)
        
        elves.rotate(-target)
        # print("Rotated:", elves)
        
        elves.popleft()
        
        elves.rotate(target)
        # print("After removal:", elves)
        # print("-----")
        
        current_elf = elves.index(elf)
        current_elf = (current_elf + 1) % len(elves)
        
        # if len(elves) % 1000 == 0:
        #     print(len(elves))
        
    return elves[0] + 1

def part2(input):
    # for i in range(1, 20):
    #     print(i, solve_circle(i))
    
    return solve_circle(3018458)
    
    # return solve_circle(5) 

if __name__ == "__main__":
    main()