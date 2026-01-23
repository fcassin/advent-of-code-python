import sys
sys.path.append("../../")

import collections
import functools
import graph
import itertools
import letter
import hashlib
import re

def main():
    with open("input.txt", "r") as input_file:
        print(part1(input_file.readlines()))

    with open("input.txt", "r") as input_file:
        print(part2(input_file.readlines()))

def part1(input):
    sum = 0
    disk = []

    file = 0
    free_space = []
    file_space = []
    pos = 0

    for line in input:
        line = line.replace('\n', '')
        if line != None:
            for current, char in enumerate(line):
                if current % 2 == 0:
                    file_space.append((pos, int(char)))
                    for _ in range(int(char)):
                        disk.append(file)
                        pos += 1
                    
                    file += 1
                else:
                    free_space.append((pos, int(char)))
                    for _ in range(int(char)):
                        disk.append(-1)
                        pos += 1

    last_replace = 0
    for file_tuple in reversed(file_space):
        file_index = file_tuple[0]
        file_length = file_tuple[1]
        file_name = disk[file_index]
        
        length = len(disk)
        
        if file_index + file_length < last_replace:
            break

        last_replace = 0
        
        for i in range(file_length):
            for j in range(last_replace, length):
                if j > file_index:
                    break

                value = disk[j]

                last_replace = j

                if value == -1:
                    disk[j] = file_name
                    disk[file_index + i] = -1

                    break

    for index, value in enumerate(disk):
        if value != -1:
            sum += index * value

    return sum

def part2(input):
    sum = 0
    disk = []

    file = 0
    free_space = []
    file_space = []
    pos = 0

    for line in input:
        line = line.replace('\n', '')
        if line != None:
            for current, char in enumerate(line):
                if current % 2 == 0:
                    file_space.append((pos, int(char)))
                    for i in range(int(char)):
                        disk.append(file)
                        pos += 1
                    
                    file += 1
                else:
                    free_space.append((pos, int(char)))
                    for i in range(int(char)):
                        disk.append(-1)
                        pos += 1

    for file_tuple in reversed(file_space):
        file_index = file_tuple[0]
        file_size = file_tuple[1]
        file_id = disk[file_index]

        for index, free_tuple in enumerate(free_space):
            free_space_size = free_tuple[1]
            if free_space_size >= file_size:
                free_index = free_tuple[0]

                if free_index < file_index:
                
                    for i in range(file_size):
                        disk[free_index + i] = file_id

                    for i in range(file_size):
                        disk[file_index + i] = -1

                    diff = free_space_size - file_size
                    
                    free_index = free_index + file_size
                    free_space_size = diff
                    free_space[index] = (free_index, free_space_size)

                    break

    for index, value in enumerate(disk):
        if value != -1:
            sum += index * value

    return sum

if __name__ == "__main__":
    main()