import collections
import hashlib

from aoc import graph, letter


def main():
    with open("input.txt", "r") as input_file:
        print(part1(input_file.readlines()))

    with open("input.txt", "r") as input_file:
        print(part2(input_file.readlines()))

left_list = []
right_list = []
right_count = collections.Counter()

def part1(input):
    for line in input:
        line = line.replace('\n', '')
        
        left, right = line.split()
        left, right = int(left), int(right)
        left_list.append(left)
        right_list.append(right)
        right_count[right] += 1

    left_list.sort()
    right_list.sort()

    result = 0
    for left, right in zip(left_list, right_list):
        result += abs(left - right)

    return result

def part2(input):
    result = 0
    
    for val in left_list:
        result += val * right_count.get(val, 0)

    return result

if __name__ == "__main__":
    main()
