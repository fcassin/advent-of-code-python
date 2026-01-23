
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

neighbours = collections.defaultdict(list)
def part1(input):
    for line in input:
        line = line.replace('\n', '')
        if line != None:
            left, right = line.split('-')

            neighbours[left].append(right)
            neighbours[right].append(left)
            

    # for p in itertools.product(neighbours["aq"], neighbours["aq"]):
    #     print(p)

    truples = set()
    for c, n in neighbours.items():
        for p in itertools.product(n, n):
            l, r = p
            if l != r:
                if c.startswith("t") or l.startswith("t") or r.startswith("t"):
                    if r in neighbours[l]:
                        truples.add(tuple(sorted((c, l, r))))

    return len(truples)

def part2(input):
    for line in input:
        line = line.replace('\n', '')
        if line != None:
            left, right = line.split('-')

            neighbours[left].append(right)
            neighbours[right].append(left)
            

    lans = list()
    for comp, neighs in neighbours.items():
        for neigh in neighs:
            inserted = False
            for lan in lans:
                if comp in lan:
                    all_connected = True
                    for oc in lan:
                        all_connected = all_connected and oc in neighbours[neigh]
                    if all_connected:
                        lan.add(neigh)
                        inserted = True
        
            if not inserted:
                lans.append(set({comp, neigh}))

    largest = None
    size = 0

    for lan in lans:
        if len(lan) > size:
            size = len(lan)
            largest = lan



    





    return ",".join(sorted(largest))

if __name__ == "__main__":
    main()