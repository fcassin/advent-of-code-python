
import sys
sys.path.append("../../")

import collections
import copy
import functools
import graph
import grid
import itertools
import letter
import hashlib
import re

map = collections.defaultdict(lambda: collections.defaultdict(str))

def main():
    with open("input.txt", "r") as input_file:
        lines = input_file.readlines()
        print(part1(lines))
        print(part2(lines))

@functools.cache
def prune(secret):
    return secret % 16777216

@functools.cache
def mix(secret, to_mix):
    return secret ^ to_mix

@functools.cache
def price(secret):
    return secret % 10
    
@functools.cache
def compute_next(secret):
    secret = mix(secret, secret * 64)
    secret = prune(secret)

    secret = mix(secret, secret // 32)
    secret = prune(secret)

    secret = mix(secret, secret * 2048)
    secret = prune(secret)

    return secret


def part1(input):
    initial_secrets = []

    for line in input:
        line = line.replace('\n', '')
        if line != None:
            initial_secrets.append(int(line))

    sum = 0
    for secret in initial_secrets:
        for i in range(2000):
            secret = compute_next(secret)
        sum += secret

    return sum

frequency = collections.defaultdict(int)
profit = collections.defaultdict(int)

def part2(input):
    initial_secrets = []

    for line in input:
        line = line.replace('\n', '')
        if line != None:
            initial_secrets.append(int(line))

    
    for secret in initial_secrets:
        seen = set()
        previous = price(secret)
        window = collections.deque(maxlen=4)
        
        for i in range(2000):
            secret = compute_next(secret)
            # print(secret, price(secret), price(secret) - previous)
            window.append(price(secret) - price(previous))
            
            if tuple(window) not in seen:
                seen.add(tuple(window))
            
                frequency[tuple(window)] += 1
                profit[tuple(window)] += price(secret)

            previous = secret

    best_profit = 0
    
    for seq, prof in profit.items():
        if prof > best_profit:
            best_profit = prof

    return best_profit

if __name__ == "__main__":
    main()