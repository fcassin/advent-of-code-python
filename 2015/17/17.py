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

@functools.cache
def sum_to_target(current, volumes, target):
    if current == target:
        return 1
    if current > target or not volumes:
        return 0
    
    # Include the first volume
    include_first = sum_to_target(current + volumes[0], volumes[1:], target)
    
    # Exclude the first volume
    exclude_first = sum_to_target(current, volumes[1:], target)
    
    return include_first + exclude_first

def combinations_to_target(acc, volumes, target):
    # print(f"Current combination: {acc}, Remaining volumes: {volumes}, Target: {target}")
    
    if sum(acc) == target:
        yield acc
        return
    if sum(acc) > target:
        return
    if not volumes:
        return
    
    yield from combinations_to_target(acc + (volumes[0],), volumes[1:], target)
    yield from combinations_to_target(acc, volumes[1:], target)
    
    return

def part1(input):
    target = 150
    volumes = []
    
    for line in input:
        line = line.replace('\n', '')
        if line:
            volumes.append(int(line))
        
    results = []    
        
    for result in combinations_to_target((), tuple(volumes), target):
        results.append(result)
        
    return len(results)

def part2(input):
    target = 150
    volumes = []
    
    for line in input:
        line = line.replace('\n', '')
        if line:
            volumes.append(int(line))
        
    results = []    
        
    for result in combinations_to_target((), tuple(volumes), target):
        results.append(result)
        
    shortest = min(len(result) for result in results)
    results = [result for result in results if len(result) == shortest]    
        
    return len(results)

if __name__ == "__main__":
    main()
