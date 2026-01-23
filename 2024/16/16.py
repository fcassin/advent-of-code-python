
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

map = collections.defaultdict(lambda:collections.defaultdict(str))
# right, down, left, up
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def valid_step(map, current, next):
    width = len(map)
    height = len(map[0])

    if next[0] >= 0 and next[0] < width and next[1] >= 0 and next[1] < height:
        if map[next[0]][next[1]] == "#":
            return False
        else:
            return True
        
    return False

def depth_walk(grid, start, end):
    best_score = 10000000

    best_paths = []

    seats = set()

    count_best_path = 0

    seen = set()
    seen_score = {}

    seen_pos = set()
    seen_pos_score = {}

    init = (start[0], start[1], 0, 0, [(start[0], start[1])])
    paths = collections.deque([(init)])
    

    iteration = 0
    while len(paths) > 0:
        iteration += 1
        
        path = paths.popleft()
        current = (path[0], path[1])
        dir_index = path[2]
        score = path[3]

        # if (iteration % 10000) == 0:
        #     print(len(paths), path)

        if (path[0], path[1], path[2]) in seen:
            if (path[0], path[1], path[2]) in seen_score:
                if path[3] > seen_score[(path[0], path[1], path[2])]:
                    continue

        if (path[0], path[1]) in seen_pos:
            if (path[0], path[1]) in seen_pos_score:
                if path[3] > seen_pos_score[(path[0], path[1])] + 2000:
                    # print("seen pos cont")
                    continue

        seen.add((path[0], path[1], path[2]))
        seen_score[(path[0], path[1], path[2])] = path[3]
        seen_pos.add((path[0], path[1]))
        seen_pos_score[(path[0], path[1])] = path[3]

        direction = directions[dir_index]
        next = (current[0]+direction[0], current[1]+direction[1])
        if valid_step(map, current, next):
            if next == end:
                if score + 1 <= best_score:
                    print("new best score", score + 1)
                    best_score = score + 1
                    count_best_path += 1

                    best_paths.append((path[4], score + 1))
            else:
                new_path = path[4][:]
                new_path.append((next[0], next[1]))
                paths.append((next[0], next[1], dir_index, score + 1, new_path))

        new_path = path[4][:]
        new_path.append((path[0], path[1]))
        paths.append((path[0], path[1], (dir_index + 1)% 4, score + 1000, new_path))
        new_path = path[4][:]
        new_path.append((path[0], path[1]))
        paths.append((path[0], path[1], (dir_index - 1)% 4, score + 1000, new_path))

    print("bast paths:", count_best_path)
    print("bast paths:", count_best_path)
    print("bast paths:", count_best_path)

    for scored_path in best_paths:
        if scored_path[1] == best_score:
             for seat in scored_path[0]:
                seats.add(seat)

    print(len(seats) + 1)
    print(len(seats) + 1)
    print(len(seats) + 1)

    return best_score


def main():
    with open("input.txt", "r") as input_file:
        lines = input_file.readlines()
        print(part1(lines))
        print(part2(lines))

def part1(input):
    count = 0

    start = (0,0)
    end = (0,0)

    for y, line in enumerate(input):
        line = line.replace('\n', '')
        if line != None:
            for x, char in enumerate(line):
                map[x][y] = char

                if char == "S":
                    start = (x, y)

                if char == "E":
                    end = (x, y)
                

    grid.display(map)

    print(start, end)

    best_score = depth_walk(map, (start[0], start[1], 0), end)
    print(best_score)
    print(best_score)
    print(best_score)

    return best_score

def part2(input):
    count = 0

    return count

if __name__ == "__main__":
    main()