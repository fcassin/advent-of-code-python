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

rules = collections.defaultdict(lambda: set())
inverted_rules = collections.defaultdict(lambda: str)

@functools.cache
def all_replacements(molecule):
    global rules
    
    replacements = set()
    for index, char in enumerate(molecule):
        if char in rules:
            for replacement_molecule in rules[char]:
                new_molecule = molecule[:index] + replacement_molecule + molecule[index + 1:]
                replacements.add(new_molecule)
                # print("Replacement:", new_molecule)
        elif index < len(molecule) - 1 and molecule[index:index + 2] in rules:
            for replacement_molecule in rules[molecule[index:index + 2]]:
                new_molecule = molecule[:index] + replacement_molecule + molecule[index + 2:]
                replacements.add(new_molecule)
                # print("Replacement:", new_molecule)
    return replacements

def part1(input):
    global rules
    
    molecule = ''
    reading_rules = True
    
    for line in input:
        line = line.replace('\n', '')
        
        if line == '':
            reading_rules = False
            continue
        
        if reading_rules:
            parts = line.split(' => ')
            rules[parts[0]].add(parts[1])
            # print("Rule:", line)
            
        else:
            molecule = line
            # print("Molecule:", line)
            
    # print("Rules:", rules)
            
    replacements = all_replacements(molecule)        
                      
    # print("Replacements:", replacements)
    # print("Number of replacements:", len(replacements)) 
        
    return len(replacements)

def part2(input):
    global rules
    global inverted_rules
    
    molecule = ''
    reading_rules = True
    
    for line in input:
        line = line.replace('\n', '')
        
        if line == '':
            reading_rules = False
            continue
        
        if reading_rules:
            parts = line.split(' => ')
            rules[parts[0]].add(parts[1])
            inverted_rules[parts[1]] = parts[0]
            
        else:
            molecule = line
    
    sorted_inverted_rules = sorted(inverted_rules.items(), key=lambda x: len(x[0]), reverse=True)
    
    operations = 0
    while molecule != 'e':
        for rule in sorted_inverted_rules:
            if rule[0] in molecule:
                molecule = molecule.replace(rule[0], rule[1], 1)
                operations += 1
                break
    
    return operations

if __name__ == "__main__":
    main()
