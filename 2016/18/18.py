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
    
def part1(input):
    cols = 10
    rows = 40
    map = collections.defaultdict(lambda:collections.defaultdict(str))
    
    for line in input:
        line = line.strip()
        
        cols = len(line)
        
        for index, char in enumerate(line):
            map[index][0] = char
    
    for y_index in range(1, rows):
        for x_index in range(cols):
            left = "."
            right = "."
            
            if x_index > 0:
                left = map[x_index-1][y_index-1]
            if x_index < cols - 1:
                right = map[x_index+1][y_index-1]    
                
            if left != right:
                map[x_index][y_index] = "^"
            else:
                map[x_index][y_index] = "."
            
    # grid.display(map)
    
    count = 0
    for x in range(cols):
        for y in range(rows):
            if map[x][y] == ".":
                count += 1
        
    return count

def part2(input):
    cols = 10
    rows = 400000
    map = collections.defaultdict(lambda:collections.defaultdict(str))
    
    for line in input:
        line = line.strip()
        
        cols = len(line)
        
        for index, char in enumerate(line):
            map[index][0] = char
    
    for y_index in range(1, rows):
        for x_index in range(cols):
            left = "."
            right = "."
            
            if x_index > 0:
                left = map[x_index-1][y_index-1]
            if x_index < cols - 1:
                right = map[x_index+1][y_index-1]    
                
            if left != right:
                map[x_index][y_index] = "^"
            else:
                map[x_index][y_index] = "."
            
    # grid.display(map)
    
    count = 0
    for x in range(cols):
        for y in range(rows):
            if map[x][y] == ".":
                count += 1
        
    return count

if __name__ == "__main__":
    main()
