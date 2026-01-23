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

def part1(input):
    decoder = collections.defaultdict(collections.Counter)
    
    for line in input:
        for index, char in enumerate(line.strip()):
            decoder[index][char] += 1

    message = [None] * len(decoder)
    for index, counter in decoder.items():
        message[index] = counter.most_common(1)[0][0]
        
    return "".join(message)

def part2(input):
    decoder = collections.defaultdict(collections.Counter)
    
    for line in input:
        for index, char in enumerate(line.strip()):
            decoder[index][char] += 1

    message = [None] * len(decoder)
    for index, counter in decoder.items():
        message[index] = counter.most_common()[-1][0]
        
    return "".join(message)

if __name__ == "__main__":
    main()