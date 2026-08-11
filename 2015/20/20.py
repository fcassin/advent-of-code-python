import collections
import functools
import itertools
import hashlib

from aoc import graph, ints, letter


def main():
    with open("input.txt", "r") as input_file:
        print(part1(input_file.readlines()))

    with open("input.txt", "r") as input_file:
        print(part2(input_file.readlines()))

@functools.lru_cache(None)
def dividers(n):
    divs = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divs.add(i)
            divs.add(n // i)
    return divs

remaining_dividers = collections.defaultdict(int)
def mapped_dividers(n):
    divs = set()
    
    for potential in range(1, int(n**0.5) + 1):
        if n % potential == 0:
            divs.add(potential)
            divs.add(n // potential)
    
    valid_divs = set()
    for divider in divs:
        if remaining_dividers[divider] < 50:
            remaining_dividers[divider] += 1
            valid_divs.add(divider)
            
    return valid_divs

def part1(input):
    for line in input:
        line = line.replace('\n', '')
        input = int(line)
    
    house = 0
    presents = 0 
    while presents < input:
        house = house + 1
        presents = sum(10 * d for d in dividers(house)) 
        
    return house

def part2(input):
    for line in input:
        line = line.replace('\n', '')
        input = int(line)
    
    house = 0
    presents = 0 
    while presents < input:
        house = house + 1
        dividers = mapped_dividers(house)
        presents = sum(11 * d for d in dividers)
        
    return house

if __name__ == "__main__":
    main()
