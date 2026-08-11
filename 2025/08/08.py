import collections
import functools
import hashlib
import itertools
import math

from aoc import graph, grid, ints, letter, screen


def main():
    with open("input.txt", "r") as input_file:
        print(part1(input_file.readlines()))

    with open("input.txt", "r") as input_file:
        print(part2(input_file.readlines()))
    
def compute_distance(box1, box2):
    x = (box1[0] - box2[0]) * (box1[0] - box2[0])
    y = (box1[1] - box2[1]) * (box1[1] - box2[1])
    z = (box1[2] - box2[2]) * (box1[2] - box2[2])
    
    return x + y + z    
    
BOXES = []    
DISTANCES = []
    
def part1(input):
    global BOXES
    global DISTANCES
    
    for line in input:
        line = line.strip()
        
        coords = ints.extract(line)
        BOXES.append(((coords[0], coords[1], coords[2])))
        
    for index in range(len(BOXES)):
        for second in range(index + 1, len(BOXES)):
            if index == second:
                continue
            
            dist = compute_distance(BOXES[index], BOXES[second])    
            DISTANCES.append((dist, index, second))
    
    DISTANCES = sorted(DISTANCES, key=lambda x: x[0])
    # print(f"Sorted distances:{DISTANCES}")
        
    circuits = []
    connections = 0
    for dist in DISTANCES:
        if connections == 1000:
            break
        
        left = None
        right = None
        found = False
        for index, circuit in enumerate(circuits):
            if dist[1] in circuit and dist[2] in circuit:
                found = True
                # connections = connections + 1
                break
            
            if dist[1] in circuit:
                left = index
                found = True
                
            if dist[2] in circuit:
                right = index
                found = True
        
        if left is not None and right is not None:
            left_set = circuits[left]
            right_set = circuits[right]
            
            circuits.remove(left_set)
            circuits.remove(right_set)
            
            new_set = left_set.union(right_set)
            circuits.append(new_set)
            
            connections = connections + 1
            
        elif found:
            if left is not None:
                circuits[left].add(dist[2])
            elif right is not None:
                circuits[right].add(dist[1])    
        
            connections = connections + 1
        
        else:
            new_circuit = set()
            new_circuit.add(dist[1])
            new_circuit.add(dist[2])
            
            connections = connections + 1
            circuits.append(new_circuit)

    circuits = sorted(circuits, key=lambda x: len(x), reverse=True)
    
    # 12696: too low
    # 283200: too high
    return len(circuits[0]) * len(circuits[1]) * len(circuits[2])

def part2(input):
    circuits = []
    connections = 0
    
    union = False
    union_at = 0
    for dist in DISTANCES:
        if union:
            break
        
        left = None
        right = None
        found = False
        for index, circuit in enumerate(circuits):
            if dist[1] in circuit and dist[2] in circuit:
                found = True
                connections = connections + 1
                break
            
            if dist[1] in circuit:
                left = index
                found = True
                
            if dist[2] in circuit:
                right = index
                found = True
        
        if left is not None and right is not None:
            left_set = circuits[left]
            right_set = circuits[right]
            
            circuits.remove(left_set)
            circuits.remove(right_set)
            
            new_set = left_set.union(right_set)
            circuits.append(new_set)
            
            connections = connections + 1
            
        elif found:
            if left is not None:
                circuits[left].add(dist[2])
            elif right is not None:
                circuits[right].add(dist[1])    
        
            connections = connections + 1
        
        else:
            new_circuit = set()
            new_circuit.add(dist[1])
            new_circuit.add(dist[2])
            
            connections = connections + 1
            circuits.append(new_circuit)
            
        if len(circuits) == 1 and len(circuits[0]) == len(BOXES):
                union = True
                union_at = BOXES[dist[1]][0] * BOXES[dist[2]][0]

    circuits = sorted(circuits, key=lambda x: len(x), reverse=True)
    
    # 12696: too low
    # 283200: too high
    return union_at

if __name__ == "__main__":
    main()
