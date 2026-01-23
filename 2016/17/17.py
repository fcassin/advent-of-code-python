import sys
sys.path.append("../../")

import collections
import functools
import graph
import grid
import ints
import itertools
import letter
import hashlib
import screen

def main():
    with open("input.txt", "r") as input_file:
        print(part1(input_file.readlines()))

    with open("input.txt", "r") as input_file:
        print(part2(input_file.readlines()))

PASSCODE = "qljzarfv"

def path_reprentation(path):
    repr = ""
    for i in range(1, len(path)):
        dx = path[i][0] - path[i-1][0]
        dy = path[i][1] - path[i-1][1]
        if dx == 1 and dy == 0:
            repr += "R"
        elif dx == -1 and dy == 0:
            repr += "L"
        elif dx == 0 and dy == 1:
            repr += "D"
        elif dx == 0 and dy == -1:
            repr += "U"
    return repr

def get_doors(path):
    if len(path) == 1:
        input = PASSCODE
    else:
        input = PASSCODE + path_reprentation(path)
        
    hash = hashlib.md5(input.encode()).hexdigest()
    
    directions = []
    if hash[3] in "bcdef":
        # right
        directions.append((1, 0))
    if hash[1] in "bcdef":
        # down
        directions.append((0, 1))
    if hash[2] in "bcdef":
        # left
        directions.append((-1, 0))
    if hash[0] in "bcdef":
        # up
        directions.append((0, -1))
        
    return directions
    
    
def part1(input):
    map = collections.defaultdict(lambda:collections.defaultdict(str))
    
    for x in range(4):
        for y in range(4):
            map[x][y] = "."
            
    # grid.display(map)
    
    starting_point = (0, 0)
    destination = (3, 3)
    
    valid_paths, _ = grid.breadth_first_search(map, grid.default_validity_walled_grid,
        get_doors, starting_point, destination, memoize=False)       
            
    return path_reprentation(valid_paths[0])

def part2(input):
    map = collections.defaultdict(lambda:collections.defaultdict(str))
    
    for x in range(4):
        for y in range(4):
            map[x][y] = "."
            
    # grid.display(map)
    
    starting_point = (0, 0)
    destination = (3, 3)
    
    valid_paths, _ = grid.breadth_first_search(map, grid.default_validity_walled_grid,
        get_doors, starting_point, destination, memoize=False, max_steps=5000)         
      
    # print(len(valid_paths))  
    # print(path_reprentation(valid_paths[-1]))
            
    return len(path_reprentation(valid_paths[-1]))

if __name__ == "__main__":
    main()