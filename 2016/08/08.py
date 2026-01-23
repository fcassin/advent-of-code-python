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

def rectangle(scr, dimensions):
    for x in range(dimensions[0]):
        for y in range(dimensions[1]):
            scr[x][y] = "#"
    
def rotate_row(scr, instuctions):
    width = len(scr)
    row, amount = instuctions
    new_row = ["."] * width
    
    for x in range(width):
        new_row[(x + amount) % width] = scr[x][row]
        
    for x in range(width):
        scr[x][row] = new_row[x]
    
def rotate_column(scr, instructions):
    height = len(scr[0])
    column, amount = instructions
    new_column = ["."] * height
    
    for y in range(height):
        new_column[(y + amount) % height] = scr[column][y]
        
    for y in range(height):
        scr[column][y] = new_column[y]    
    
def count_pixels(scr):
    count = 0
    
    for x in range(len(scr)):
        for y in range(len(scr[0])):
            if scr[x][y] == "#":
                count += 1
                
    return count    
    
scr = []
    
for x in range(50):
    scr.append(["."] * 6)    
    
def part1(input):
    for line in input:
        line = line.strip()
        
        if line.startswith("rect"):
            dimensions = ints.extract(line)
            rectangle(scr, dimensions)
        elif line.startswith("rotate row"):
            instructions = ints.extract(line)
            rotate_row(scr, instructions)
        elif line.startswith("rotate column"):
            instructions = ints.extract(line)
            rotate_column(scr, instructions)
        
    return count_pixels(scr)

def part2(input):
    return screen.read_letters_from_grid(scr)

if __name__ == "__main__":
    main()