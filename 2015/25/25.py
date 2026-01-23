import sys
sys.path.append("../../")

import collections
import functools
import graph
import ints
import itertools
import letter
import hashlib

def main():
    with open("input.txt", "r") as input_file:
        print(part1(input_file.readlines()))

    with open("input.txt", "r") as input_file:
        print(part2(input_file.readlines()))

def summation(n):
    return n * (n + 1) // 2

def position(x, y):
    diag = x + y - 1
    return summation(diag - 1) + y

def part1(input):
    # 2978, 3083
    iterations = position(2978, 3083)
    code = 20151125
    for _ in range(1, iterations):
        code = (code * 252533) % 33554393
        
    return code

def part2(input):
    return 0

if __name__ == "__main__":
    main()