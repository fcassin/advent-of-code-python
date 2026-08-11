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

def supports_tls(parts):
    supports_tls = False
    
    for index, part in enumerate(parts):
        if len(part) < 4:
            continue
        for i in range(len(part) - 3):
            if part[i] != part[i+1] and part[i] == part[i+3] and part[i+1] == part[i+2]:
                if index % 2 == 0:
                    supports_tls = True
                else:
                    return False
    return supports_tls

def supports_ssl(parts):
    abas = set()
    babs = set()
    
    for index, part in enumerate(parts):
        if len(part) < 3:
            continue
        
        for i in range(len(part) - 2):
            if part[i] != part[i+1] and part[i] == part[i+2]:
                if index % 2 == 0:
                    abas.add(part[i:i+3])
                else:
                    babs.add(part[i:i+3])
    
    for aba in abas:
        bab = aba[1] + aba[0] + aba[1]
        
        if bab in babs:
            return True
    return False
    
def part1(input):
    count = 0
    
    for line in input:
        line = line.strip()
        line = line.replace("[", " ").replace("]", " ")
        parts = line.split(" ")
        
        if supports_tls(parts):
            count += 1
        
    return count

def part2(input):
    count = 0
    
    for line in input:
        line = line.strip()
        line = line.replace("[", " ").replace("]", " ")
        parts = line.split(" ")
        
        print("parts:", parts, supports_ssl(parts))
        
        if supports_ssl(parts):
            count += 1

    return count

if __name__ == "__main__":
    main()
