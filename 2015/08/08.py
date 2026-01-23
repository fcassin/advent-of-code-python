import collections
import hashlib

def main():
    with open("input.txt", "r") as input_file:
        print(part1(input_file.readlines()))

    with open("input.txt", "r") as input_file:
        print(part2(input_file.readlines()))

def count(line):
    code_count = 0
    string_count = len(line)
    
    i = 0
    while i < len(line):
        if line[i] == "\\" and line[i + 1] == "\"":
            code_count = code_count + 1
            i = i + 2
            continue

        if line[i] == "\\" and line[i + 1] == "\\":
            code_count = code_count + 1
            i = i + 2
            continue

        if line[i] == "\\" and line[i + 1] == "x":
            code_count = code_count + 1
            i = i + 4
            continue

        if line[i] == "\"":
            i = i + 1
            continue
            
        i = i + 1
        code_count = code_count + 1

    return (string_count, code_count)

def encode(line):
    code_count = 2 # for the "s
    string_count = len(line)
    
    i = 0
    while i < len(line):
        if line[i] == "\"":
            code_count = code_count + 1
        elif line[i] == "\\":
            code_count = code_count + 1

        code_count = code_count + 1
        i = i + 1

    return (string_count, code_count)


def part1(input):
    string_count = 0
    code_count = 0

    for line in input:
        line = line.replace("\n", "")
        s, c = count(line)
        string_count = string_count + s
        code_count = code_count + c
    
    return string_count - code_count

def part2(input):
    string_count = 0
    code_count = 0

    for line in input:
        line = line.replace("\n", "")
        s, c = encode(line)
        string_count = string_count + s
        code_count = code_count + c
    
    return code_count - string_count

if __name__ == "__main__":
    main()