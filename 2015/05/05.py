import collections
import hashlib

def main():
    with open("input.txt", "r") as input_file:
        print(part1(input_file))

    with open("input.txt", "r") as input_file:
        print(part2(input_file))

def nice(input):
    if sum(map(input.count, "aeiou")) < 3:
        return False

    double = False
    previous = "."
    for char in input:
        if char == previous:
            double = True
            break

        previous = char
    if not double:
        return False

    if "ab" in input:
        return False
    
    if "cd" in input:
        return False
    
    if "pq" in input:
        return False
    
    if "xy" in input:
        return False

    return True

def nicer(input):
    double = False
    for i in range(0, len(input) - 1):
        test = input[i] + input[i+1]

        if input.count(test) > 1:
            double = True
            break

    if not double:
        return False
    
    split = False
    for i in range(0, len(input) - 2):
        if input[i] == input[i+2]:
            split = True
            break

    if not split:
        return False

    return True

def part1(input):
    count = 0
    
    for line in input:
        line = line.replace("\n", "")

        if nice(line):
            count = count + 1

    return count

def part2(input):
    count = 0
    
    for line in input:
        line = line.replace("\n", "")

        if nicer(line):
            count = count + 1

    return count

if __name__ == "__main__":
    main()