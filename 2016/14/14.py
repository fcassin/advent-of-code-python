import collections
import functools
import itertools
import hashlib

from aoc import graph, grid, ints, letter, screen


def main():
    with open("input.txt", "r") as input_file:
        print(part1(input_file.readlines()))

    with open("input.txt", "r") as input_file:
        print(part2(input_file.readlines()))

@functools.lru_cache()
def hash(salt, index=None):
    if index is None:
        to_hash = salt
    else:
        to_hash = salt + str(index)
    return hashlib.md5(to_hash.encode()).hexdigest()

@functools.lru_cache()
def stretched_hash(salt, index):
    result = hash(salt, index)
    for _ in range(2016):
        result = hash(result)
    return result

@functools.lru_cache()
def is_key(string, char):
    for pos in range(len(string)):
        if pos + 4 < len(string) and string[pos] == char == string[pos + 1] == string[pos + 2] == string[pos + 3] == string[pos + 4]:
            return True
    return False

def part1(input):
    for line in input:
        salt = line.strip()
        
    keys = []
    
    index = 0
    while len(keys) < 64:
        current = hash(salt, index)
        
        triplet_char = None
        for pos, char in enumerate(current):
            if pos + 2 < len(current) and char == current[pos + 1] == current[pos + 2]:
                triplet_char = char
                break
            
        if triplet_char:
            for future_index in range(index + 1, index + 1001):
                future_hash = hash(salt, future_index)
                if is_key(future_hash, triplet_char):
                    keys.append((index, current))
                    break
        
        index = index + 1
        
    return keys[63][0]

def part2(input):
    for line in input:
        salt = line.strip()
        
    keys = []
    
    index = 0
    while len(keys) < 64:
        current = stretched_hash(salt, index)
        
        triplet_char = None
        for pos, char in enumerate(current):
            if pos + 2 < len(current) and char == current[pos + 1] == current[pos + 2]:
                triplet_char = char
                break
            
        if triplet_char:
            for future_index in range(index + 1, index + 1001):
                future_hash = stretched_hash(salt, future_index)
                if is_key(future_hash, triplet_char):
                    keys.append((index, current))
                    break
        
        index = index + 1
        
    return keys[63][0]

if __name__ == "__main__":
    main()
