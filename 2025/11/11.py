import collections
import functools
# import grid
import hashlib
import itertools
import math
# import png
# import z3

from aoc import graph, ints, letter, screen


def main():
    # with open("input.txt", "r") as input_file:
    #     print(part1(input_file.readlines()))

    with open("input.txt", "r") as input_file:
        print(part2(input_file.readlines()))
    
def part1(input):
    vertices = set()
    edges = collections.defaultdict(list)
    
    for line in input:
        line = line.strip()
        line = line.replace(":", "").split()
        
        vertice = line.pop(0)
        vertices.add(vertice)
        
        for neighbor in line:
            edges[vertice].append(neighbor)
            
    print(vertices)
    print(edges)
    
    paths = 0
    stack = collections.deque()
    stack.append("you")
    
    while len(stack) > 0:
        node = stack.pop()
        
        if node == "out":
            paths = paths + 1
            continue
        
        for neighbor in edges[node]:
            stack.append(neighbor)    
        
    return paths

VERTICES = set()
EDGES = collections.defaultdict(list)

@functools.cache
def paths(start, stop):
    global EDGES
    
    if start == stop:
        return 1
    
    accumulator = 0
    for step in EDGES.get(start, []):
        accumulator = accumulator + paths(step, stop)
    
    return accumulator

def part2(input):
    global VERTICES
    global EDGES
        
    for line in input:
        line = line.strip()
        line = line.replace(":", "").split()
        
        vertice = line.pop(0)
        VERTICES.add(vertice)
        
        for neighbor in line:
            EDGES[vertice].append(neighbor)
            
    # 11315 * 4099825 * 8281
    # 384151614084875
    
    # return 0
    return paths('svr','fft') * paths('fft','dac') * paths('dac','out')

if __name__ == "__main__":
    main()
