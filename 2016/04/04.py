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

def is_valid_room(name, checksum):
    char_count = collections.Counter(name.replace("-", ""))
    common_chars = sorted(char_count.items(), key=lambda item: (-item[1], item[0]))
    computed_checksum = "".join([char for char, count in common_chars[:5]])
    return computed_checksum in checksum

def part1(input):
    sum = 0
     
    for line in input:
        name, info = line.rsplit("-", 1)
        info = info.replace("]", "")
        zone, checksum = info.split("[")
    
        if is_valid_room(name, checksum):
            sum += int(zone)
        
    return sum

def transform_name(name, zone):
    shift = int(zone) % 26
    result = []
    for char in name:
        if char == "-":
            result.append(" ")
        else:
            new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            result.append(new_char)
    return "".join(result)

def part2(input):
    sector = 0
     
    for line in input:
        name, info = line.rsplit("-", 1)
        info = info.replace("]", "")
        zone, checksum = info.split("[")
    
        if is_valid_room(name, checksum):
            transformed_name = transform_name(name, zone)
            if "northpole object storage" in transformed_name:
                sector = int(zone)
            
    return sector

if __name__ == "__main__":
    main()
