import sys
sys.path.append("../../")

import collections
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

def distance(reindeer, time):
    total_time = reindeer['time'] + reindeer['rest']
    full_cycles = time // total_time
    remaining_time = time % total_time
    distance = full_cycles * reindeer['time'] * reindeer['speed']
    
    if remaining_time > reindeer['time']:
        distance += reindeer['time'] * reindeer['speed']
    else:
        distance += remaining_time * reindeer['speed']
    
    return distance

def part1(input):
    max_distance = 0
    reindeers = list()
    
    for line in input:
        line = line.replace('\n', '')
        
        line = line.split(' ')
        name = line[0]
        speed = int(line[3])
        time = int(line[6])
        rest = int(line[13])
        
        reindeer = {
            'name': name,
            'speed': speed,
            'time': time,
            'rest': rest
        }
        reindeers.append(reindeer)
        
        max_distance = max(max_distance, distance(reindeer, 2503))
        
    return max_distance

def scored_race(reindeers, time):
    scores = {reindeer['name']: 0 for reindeer in reindeers}
    
    for t in range(1, time + 1):
        distances = {reindeer['name']: distance(reindeer, t) for reindeer in reindeers}
        max_distance = max(distances.values())
        
        for name, dist in distances.items():
            if dist == max_distance:
                scores[name] += 1
                
    return scores

def part2(input):
    reindeers = list()
    
    for line in input:
        line = line.replace('\n', '')
        
        line = line.split(' ')
        name = line[0]
        speed = int(line[3])
        time = int(line[6])
        rest = int(line[13])
        
        reindeer = {
            'name': name,
            'speed': speed,
            'time': time,
            'rest': rest
        }
        reindeers.append(reindeer)
        
    return max(scored_race(reindeers, 2503).values())

if __name__ == "__main__":
    main()