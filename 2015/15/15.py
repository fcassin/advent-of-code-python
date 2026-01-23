import sys
sys.path.append("../../")

import collections
import functools
import graph
import ints
import itertools
import letter
import hashlib

def main():
    with open("input.txt", "r") as input_file:
        print(part1(input_file.readlines()))

    with open("input.txt", "r") as input_file:
        print(part2(input_file.readlines()))

def score(ingredients, possibility):
    capacity = 0
    durability = 0
    flavor = 0
    texture = 0
    
    for i in range(len(ingredients)):
        capacity += ingredients[i]['capacity'] * possibility[i]
        durability += ingredients[i]['durability'] * possibility[i]
        flavor += ingredients[i]['flavor'] * possibility[i]
        texture += ingredients[i]['texture'] * possibility[i]
        
    if capacity < 0:
        capacity = 0
    if durability < 0:
        durability = 0
    if flavor < 0:
        flavor = 0
    if texture < 0:
        texture = 0
    
    return capacity * durability * flavor * texture

def count_calories(ingredients, possibility):
    calories = 0
    
    for i in range(len(ingredients)):
        calories += ingredients[i]['calories'] * possibility[i]
    
    return calories

def part1(input):
    ingredients = list()
    
    for line in input:
        line = line.replace('\n', '')
        line = line.replace(',', '')
        line = line.replace(':', '')
        line = line.split(' ')
        
        ingredient = {
            'name': line[0],
            'capacity': int(line[2]),
            'durability': int(line[4]),
            'flavor': int(line[6]),
            'texture': int(line[8]),
            'calories': int(line[10])
        }
        
        ingredients.append(ingredient)
        
    best_score = 0
    for possibility in itertools.product(range(101), repeat=len(ingredients)):
        if sum(possibility) == 100:
            possible_score = score(ingredients, possibility)
            if possible_score > best_score:
                best_score = possible_score
                
    # for possibility in itertools.combinations_with_replacement(range(101), len(ingredients)):
    #     if sum(possibility) == 100:
    #         possible_score = score(ingredients, possibility)
    #         if possible_score > best_score:
    #             best_score = possible_score
        
    return best_score

def part2(input):
    ingredients = list()
    
    for line in input:
        line = line.replace('\n', '')
        line = line.replace(',', '')
        line = line.replace(':', '')
        line = line.split(' ')
        
        ingredient = {
            'name': line[0],
            'capacity': int(line[2]),
            'durability': int(line[4]),
            'flavor': int(line[6]),
            'texture': int(line[8]),
            'calories': int(line[10])
        }
        
        ingredients.append(ingredient)
        
    best_score = 0
    
    for possibility in itertools.product(range(101), repeat=len(ingredients)):
        if sum(possibility) == 100:
            if count_calories(ingredients, possibility) == 500:
                possible_score = score(ingredients, possibility)
                if possible_score > best_score:
                    best_score = possible_score
    
    # for possibility in itertools.combinations_with_replacement(range(101), len(ingredients)):
    #     if sum(possibility) == 100:
    #         if count_calories(ingredients, possibility) == 500:
    #             
    #             possible_score = score(ingredients, possibility)
    #             if possible_score > best_score:
    #                 best_score = possible_score
        
    # 27 27 15 31
    # Correct answer is 11171160, but I always get 11162880
    return best_score

if __name__ == "__main__":
    main()