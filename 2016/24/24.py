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

MAP = collections.defaultdict(lambda: collections.defaultdict(str))
DISTANCE_BETWEEN_POINTS = collections.defaultdict(lambda: collections.defaultdict(int))

def main():
    with open("input.txt", "r") as input_file:
        print(part1(input_file.readlines()))

    with open("input.txt", "r") as input_file:
        print(part2(input_file.readlines()))
    
def part1(input):
    pois = {}
    
    for y, line in enumerate(input):
        line = line.strip()
        
        for x, char in enumerate(line):
            MAP[x][y] = char
            
            if char not in ['#', '.']:
                point_of_interest = (x, y)
                pois[int(char)] = point_of_interest
                
    grid.display(MAP)
    
    total_steps = 0
    current_point = 0
    
    global DISTANCE_BETWEEN_POINTS
    
    while len(pois) > 1:
        starting_point = pois.pop(current_point) 
        shortest_target = None
        
        for key, value in pois.items():
            shortest, distances = grid.breadth_first_search(MAP, 
                grid.default_validity_walled_grid,
                grid.default_directions,
                starting_point, 
                value)
            
            DISTANCE_BETWEEN_POINTS[current_point][key] = len(shortest[0]) - 1
            DISTANCE_BETWEEN_POINTS[key][current_point] = len(shortest[0]) - 1
            
            if shortest_target is None or len(shortest[0]) <= len(shortest_target[1]):
                shortest_target = (key, shortest[0])
   
        total_steps += len(shortest_target[1]) - 1
        current_point = shortest_target[0]
    
    vertices = []
    edges = []
    for x in DISTANCE_BETWEEN_POINTS:
        for y in DISTANCE_BETWEEN_POINTS[x]:
            if x not in vertices:
                vertices.append(x)
            if y not in vertices:
                vertices.append(y)
            edges.append((x, y, DISTANCE_BETWEEN_POINTS[x][y]))
            
    min_cost, optimal_route = graph.travelling_salesman_no_return(vertices, edges, origin=0)

    return min_cost

def part2(input):
    vertices = []
    edges = []
    
    global DISTANCE_BETWEEN_POINTS
    
    for x in DISTANCE_BETWEEN_POINTS:
        for y in DISTANCE_BETWEEN_POINTS[x]:
            if x not in vertices:
                vertices.append(x)
            if y not in vertices:
                vertices.append(y)
            edges.append((x, y, DISTANCE_BETWEEN_POINTS[x][y]))
            
    min_cost, optimal_route = graph.travelling_salesman(vertices, edges, origin=0)

    return min_cost

if __name__ == "__main__":
    main()