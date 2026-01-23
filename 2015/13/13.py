import sys
sys.path.append("../../")

import collections
import graph
import ints
import itertools
import letter
import hashlib

import json

def main():
    with open("input.txt", "r") as input_file:
        print(part1(input_file.readlines()))

    with open("input.txt", "r") as input_file:
        print(part2(input_file.readlines()))

def part1(input):
    persons = set()
    happiness = {}
    
    for line in input:
        line = line.replace('\n', '')
        data = line.split(' ')
        
        person = data[0]
        relationship = data[2]
        amount = data[3]
        other = data[10].replace('.', '')
        
        persons.add(data[0])
        
        if relationship == 'lose':
            amount = -int(amount)
        else:
            amount = int(amount)
            
        if happiness.get(person) is None:
            happiness[person] = {}
            
        happiness[person][other] = amount
        
    iterations = itertools.permutations(persons)
    best = 0
    for iteration in iterations:
        total = 0
        
        for index, person in enumerate(iteration):
            left = person
            right = iteration[(index + 1) % len(iteration)]
            
            total += happiness.get(left, {}).get(right, 0)
            total += happiness.get(right, {}).get(left, 0)
            
        if total > best:
            best = total

    return best

def part2(input):
    persons = set()
    happiness = {}
    
    for line in input:
        line = line.replace('\n', '')
        data = line.split(' ')
        
        person = data[0]
        relationship = data[2]
        amount = data[3]
        other = data[10].replace('.', '')
        
        persons.add(data[0])
        
        if relationship == 'lose':
            amount = -int(amount)
        else:
            amount = int(amount)
            
        if happiness.get(person) is None:
            happiness[person] = {}
            
        happiness[person][other] = amount
        happiness[person]['me'] = 0
        
    persons.add('me')
    iterations = itertools.permutations(persons)
    best = 0
    for iteration in iterations:
        total = 0
        
        for index, person in enumerate(iteration):
            left = person
            right = iteration[(index + 1) % len(iteration)]
            
            total += happiness.get(left, {}).get(right, 0)
            total += happiness.get(right, {}).get(left, 0)
            
        if total > best:
            best = total

    return best

if __name__ == "__main__":
    main()