import collections
import functools
import itertools
import hashlib

from aoc import graph, grid, ints, letter, screen


def main():
    with open("input.txt", "r") as input_file:
        print(part1(input_file.readlines()))

    with open("input.txt", "r") as input_file:
        print(part2(input_file.readlines()))
    
class Node:
    def __init__(self, size, used, avail):
        self.size = size
        self.used = used
        self.avail = avail
        
    def __repr__(self):
        return f"Node(size={self.size}, used={self.used}, avail={self.avail})"
    
map = collections.defaultdict(lambda: collections.defaultdict(Node))    
    
def viable_pair(a, b):
    if a == b:
        return False
    if a.used == 0:
        return False
    if a.used <= b.avail:
        return True
    return False
    
def part1(input):
    for line in input:
        line = line.strip()
        
        values = ints.extract(line)
        if len(values) != 6:
            continue
        
        x, y = values[0], values[1]
        node = Node(size=values[2], used=values[3], avail=values[4])
        
        map[x][y] = node
        
    # for x in map:
    #     for y in map[x]:
    #         print(f"({x},{y}): {map[x][y]}")
        
    pair_count = 0    
        
    for ax in map:
        for ay in map[ax]:
            a = map[ax][ay]
            
            for bx in map:
                for by in map[bx]:
                    b = map[bx][by]
                    
                    if viable_pair(a, b):
                        pair_count += 1    
    
    # 661 is too low
    # 674 is too low
    return pair_count

def part2(input):
    # One empty node at (35,18)
    # /dev/grid/node-x35-y18   85T    0T    85T    0%
    
    for line in input:
        line = line.strip()
        
        values = ints.extract(line)
        if len(values) != 6:
            continue
        
        x, y = values[0], values[1]
        node = Node(size=values[2], used=values[3], avail=values[4])
        
        if node.used == 0:
            map[x][y] = '_'
        elif node.used > 100:
            map[x][y] = '#'
        else:
            map[x][y] = '.'
        
    # grid.display(map)
    # BFS could be used to find 62
    # Then can we really use a known algorithm to move data to the target?
    # Or are we better served to notice that 5 moves are required to move 
    # the data one step to the left? Adding a final step once everything is in place.
    
    # 62 steps to move empty node to (0,23)
    # 35 * 5 = 180 steps to move goal data to (0,0)
    # 1 last move
    
    return 238

if __name__ == "__main__":
    main()
