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
    numbers = []
    operands = []
    
    for line in input:
        line = line.strip()
        
        if "+" in line:
            operands = line.split()
            
        else:
            numbers.append(ints.extract(line))
        
    total = 0
    for index, operand in enumerate(operands):
        compute = 0
        if operand == "*":
            compute = 1
        
        for number in numbers:
            if operand == "+":
                compute = compute + number[index]
            elif operand == "*":
                compute = compute * number[index]
        
        total = total + compute
        
    return total

def part2(input):
    numbers = []
    operands = []
    
    length = 0
    raw_numbers = []
    raw_operands = []
    for line in input:
        length = max(length, len(line))
        
        if "+" in line:
            raw_operands = line
        else:
            raw_numbers.append(line)
    
    index = 0
    current_numbers = []
    while index < length:
        if index < len(raw_operands) and raw_operands[index] != " ":
            operands.append(raw_operands[index])
        
        buffer = ""
        
        for nums in raw_numbers:
            if nums[index] != " " and nums[index] != "\n":
                buffer = buffer + nums[index]
                all_empty = False
            
        if buffer != "":
            current_numbers.append(int(buffer))
        else:
            numbers.append(current_numbers)
            current_numbers = []
                
        index = index + 1
        
    total = 0
    for index, operand in enumerate(operands):
        compute = 0
        if operand == "*":
            compute = 1
        
        for number in reversed(numbers[index]):
            if operand == "+":
                compute = compute + number
            elif operand == "*":
                compute = compute * number
                
        total = total + compute
        
    return total

if __name__ == "__main__":
    main()
