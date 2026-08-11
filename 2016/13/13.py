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
    
def is_wall(x, y, favorite_number):
    value = x*x + 3*x + 2*x*y + y + y*y + favorite_number
    bits = bin(value).count("1")
    return bits % 2 == 1    
    
def part1(input):
    favorite_number = 1358
    map = collections.defaultdict(lambda:collections.defaultdict(str))
        
    for x  in range(60):
        for y in range(60):
            wall = is_wall(x, y, favorite_number)
            if wall:
                map[x][y] = "#"
            else:
                map[x][y] = "."
                
    # grid.display(map)
    
    starting_point = (1, 1)
    valid_paths, _ = grid.breadth_first_search(map, grid.default_validity_walled_grid,
        grid.default_directions, starting_point, (31,39))
        
    return len(valid_paths[0]) - 1

def part2(input):
    favorite_number = 1358
    map = collections.defaultdict(lambda:collections.defaultdict(str))
        
    for x  in range(60):
        for y in range(60):
            wall = is_wall(x, y, favorite_number)
            if wall:
                map[x][y] = "#"
            else:
                map[x][y] = "."
    
    starting_point = (1, 1)
    valid_paths, shortest_paths = grid.breadth_first_search(map, grid.default_validity_walled_grid,
        grid.default_directions, starting_point, (31,39))
    
    reachable_locations = 0
    for location, distance in shortest_paths.items():
        _ = location
        
        if distance <= 50:
            reachable_locations += 1
        
    return reachable_locations

if __name__ == "__main__":
    main()
