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
    
class Vertex:
    def __init__(self):
        self.floors = [set() for _ in range(4)]
        self.elevator = 0
    
class Radioisotope:
    def __init__(self, element, type):
        self.element = element
        self.type = type  # "G" for generator, "M" for microchip
        
def is_valid(vertex):
    for floor in vertex.floors:
        generators = [item.element for item in floor if item.type == "G"]
        microchips = [item.element for item in floor if item.type == "M"]
        
        if generators:
            for microchip in microchips:
                if microchip not in generators:
                    return False
    return True        
        
def neighbors(vertex):
    neighbor_vertices = []
    # Move elevator up or down one floor
    for direction in [-1, 1]:
        new_elevator = vertex.elevator + direction
        if 0 <= new_elevator < 4:
            # Get all combinations of 1 or 2 items on the current floor
            current_floor_items = list(vertex.floors[vertex.elevator])
            for r in [1, 2]:
                for items_to_move in itertools.combinations(current_floor_items, r):
                    new_vertex = Vertex()
                    new_vertex.elevator = new_elevator
                    # Copy floors
                    for i in range(4):
                        new_vertex.floors[i] = set(vertex.floors[i])
                    # Move items
                    for item in items_to_move:
                        new_vertex.floors[vertex.elevator].remove(item)
                        new_vertex.floors[new_elevator].add(item)
                    # Check if the new configuration is valid
                    if is_valid(new_vertex):
                        neighbor_vertices.append(new_vertex)
                        
    neighbor_vertices.reverse()
    return neighbor_vertices

def goal(vertex):
    return len(vertex.floors[0]) == 0 and len(vertex.floors[1]) == 0 and len(vertex.floors[2]) == 0

def hash(vertex):
    floor_hashes = []
    
    for floor in vertex.floors:
        generators = [item.element for item in floor if item.type == "G"]
        microchips = [item.element for item in floor if item.type == "M"]
    
        floor_hashes.append(len(generators) * 100 + len(microchips))
    
    state_hash = (vertex.elevator, tuple(floor_hashes))
    return state_hash
    
def part1(input):
    start = Vertex()
    
    for floor, line in enumerate(input):
        line = line.strip()
        line = line.split(" ")
        
        gen_indices = [i for i, val in enumerate(line) if "generator" in val]
        micro_indices = [i for i, val in enumerate(line) if "microchip" in val]
        
        for gen_index in gen_indices:
            element = line[gen_index - 1]
            radioisotope = Radioisotope(element, "G")
            start.floors[floor].add(radioisotope)
        for micro_index in micro_indices:
            element = line[micro_index - 1].split("-")[0]
            radioisotope = Radioisotope(element, "M")
            start.floors[floor].add(radioisotope)
        
    return graph.bfs(start, goal, hash, neighbors)

def part2(input):
    start = Vertex()
    
    for floor, line in enumerate(input):
        line = line.strip()
        line = line.split(" ")
        
        gen_indices = [i for i, val in enumerate(line) if "generator" in val]
        micro_indices = [i for i, val in enumerate(line) if "microchip" in val]
        
        for gen_index in gen_indices:
            element = line[gen_index - 1]
            radioisotope = Radioisotope(element, "G")
            start.floors[floor].add(radioisotope)
        for micro_index in micro_indices:
            element = line[micro_index - 1].split("-")[0]
            radioisotope = Radioisotope(element, "M")
            start.floors[floor].add(radioisotope)
        
    start.floors[0].add(Radioisotope("elerium", "G"))
    start.floors[0].add(Radioisotope("elerium", "M"))
    start.floors[0].add(Radioisotope("dilithium", "G"))
    start.floors[0].add(Radioisotope("dilithium", "M"))    
        
    return graph.bfs(start, goal, hash, neighbors)

if __name__ == "__main__":
    main()
