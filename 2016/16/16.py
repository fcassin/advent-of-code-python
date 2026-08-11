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

def dragon_curve(data):
    reversed = data[::-1].translate(str.maketrans("01", "10"))
    return data + "0" + reversed

def checksum(data):
    new_data = []
    for index, char in enumerate(data):
        if index % 2 == 0:
            pair = data[index:index+2]
            if pair[0] == pair[1]:
                new_data.append("1")
            else:
                new_data.append("0")
                
    new_data = "".join(new_data)            
                
    if len(new_data) % 2 == 0:
        return checksum(new_data)
    
    return new_data
    
def part1(input):
    _ = input
    
    disk_size = 272
    data = "00111101111101000"
    
    while len(data) < disk_size:
        data = dragon_curve(data)
        
    return checksum(data[:disk_size])

def part2(input):
    _ = input
    
    disk_size = 35651584
    data = "00111101111101000"
    
    while len(data) < disk_size:
        data = dragon_curve(data)
        
    return checksum(data[:disk_size])

if __name__ == "__main__":
    main()
