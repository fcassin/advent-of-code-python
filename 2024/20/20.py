import collections
import copy
import functools
import itertools
import hashlib
import re

from aoc import graph, grid, letter


map = collections.defaultdict(lambda: collections.defaultdict(str))

def main():
    with open("input.txt", "r") as input_file:
        lines = input_file.readlines()
        print(part1(lines))
        print(part2(lines))

# TODO move those cardinal directions to grid.py
# right, down, left, up
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def valid_step(map, next):
    width = len(map)
    height = len(map[0])

    if next[0] >= 0 and next[0] < width and next[1] >= 0 and next[1] < height:
        if map[next[0]][next[1]] == "#":
            return False
        
        return True
        
    return False

def valid_cheat(map, next):
    width = len(map)
    height = len(map[0])

    if next[0] >= 0 and next[0] < width and next[1] >= 0 and next[1] < height:
        return True
        
    return False

# manhattan distance
def dist_func(map, start, end):
    # TODO: abs might be required for a generic func
    return (end[0] - start[0]) + (end[1] - start[1])

@functools.cache
def a_star(start, end):
    paths = collections.deque([(start[0], start[1], 0, [(start[0], start[1])])])
    seen = set()

    seen.add(start)

    while len(paths) > 0:
        path = paths.popleft()
        current = (path[0], path[1])
        travelled = path[2]

        candidates = []
        for direction in directions:
            next = (current[0] + direction[0], current[1] + direction[1])

            if next in seen:
                continue
            seen.add(next)

            if valid_step(map, next):
                candidates.append((dist_func(map, current, end), (next[0], next[1])))

                if (next[0], next[1]) == end:
                    return (next[0], next[1], travelled + 1, path[3])
        
        # sort and append
        candidates = sorted(candidates)
        # print("candidates:", candidates)
        for candidate in candidates:
            paths.append((candidate[1][0], candidate[1][1], travelled + 1, path[3] + [(candidate[1][0], candidate[1][1])]))

    return None

# def cheat_search(map, valid_func, directions, starting_coordinate, target_coordinate, best):
#     valid_paths = []
# 
#     start = [starting_coordinate]
#     paths = [(False, start)]
# 
#     while len(paths) > 0:
#         # print(paths)
#         path = paths.pop()
#         has_cheated = path[0]
#         current = path[1][len(path[1]) - 1]
# 
#         if len(current) >= best:
#             continue
# 
#         for direction in directions:
#             next = (current[0] + direction[0], current[1] + direction[1])
# 
#             if valid_func(map, current, next) and next not in path[1]:
#                 new_path = copy.deepcopy(path[1])
#                 new_path.append(next)
# 
#                 if (next[0],next[1]) == target_coordinate:
#                     valid_paths.append(len(new_path))
#                 else:
#                     paths = [(has_cheated, new_path)] + paths
# 
#         if not has_cheated:
#             for dir in directions:
#                 for next_dir in directions:
#                     next = (current[0] + dir[0], current[1] + dir[1])
#                     next_next = (next[0] + next_dir[0], next[1] + next_dir[1])
# 
#                     # if valid_cheat(map, current, next) and valid_step(map, current, next_next):
#                     if valid_cheat(map, current, next) and valid_step(map, current, next_next) and next_next not in path[1]:
#                         next_path = copy.deepcopy(path[1])
#                         next_path.append(next)
#                         next_path.append(next_next)
# 
#                         if (next_next[0],next_next[1]) == target_coordinate:
#                             valid_paths.append(len(next_path) - 1)
#                         else:
#                             current_path_len = len(next_path)
#                             # print(next_next)
#                             _, _, remaining_to_end = a_star(next_next, target_coordinate)
#                             # print(current_path_len, remaining_to_end)
#                             
#                             valid_paths.append(current_path_len + remaining_to_end - 1)
# 
#                             # paths = [(True, next_path)] + paths
# 
#         
# 
# 
#     return valid_paths

def cheat_search_dist(target_coordinate, best_path):
    valid_paths = []

    
    for steps, pos in enumerate(best_path):
        seen = set()

        for dir in directions:
            for next_dir in directions:
                if (dir, next_dir) in seen:
                    continue
                seen.add((dir, next_dir))

                next = (pos[0] + dir[0], pos[1] + dir[1])
                next_next = (next[0] + next_dir[0], next[1] + next_dir[1])

                if valid_cheat(map, next) and valid_step(map, next_next):
                    if (next_next[0],next_next[1]) == target_coordinate:
                        valid_paths.append(steps + 2)
                    else:
                        # print(next_next)
                        # TODO: Flood fill from the target to all valid positions
                        # to compute distances?
                        # _, _, remaining_to_end, _ = a_star(next_next, target_coordinate)
                        # print(current_path_len, remaining_to_end)
                        
                        remaining_to_end = distances[next_next[0]][next_next[1]]
                        full_steps = steps + remaining_to_end + 2
                        
                        valid_paths.append(full_steps)

                        # paths = [(True, next_path)] + paths

    return valid_paths

@functools.cache
def a_star_dist(start, end):
    paths = collections.deque([(start[0], start[1], 0)])
    
    seen = set()
    seen.add(start)

    while len(paths) > 0:
        path = paths.popleft()
        current = (path[0], path[1])
        travelled = path[2]

        candidates = []
        for direction in directions:
            next = (current[0] + direction[0], current[1] + direction[1])

            if next in seen:
                continue
            seen.add(next)

            if valid_step(map, next):
                if distances[next[0]][next[1]] != 0:
                    return None, None, travelled + distances[next[0]][next[1]] + 1

                candidates.append((dist_func(map, current, end), (next[0], next[1])))

                if (next[0], next[1]) == end:
                    return (next[0], next[1], travelled)
        
        # sort and append
        candidates = sorted(candidates)
        # print("candidates:", candidates)
        for candidate in candidates:
            paths.append((candidate[1][0], candidate[1][1], travelled + 1))

    return None, None, None

def flood_dist(end):
    paths = collections.deque([(end, 0)])

    seen = set()
    seen.add(end)

    while len(paths) > 0:
        pos, dist = paths.popleft()

        candidates = []
        for dir in directions:
            next = (pos[0] + dir[0], pos[1] + dir[1])

            if next in seen:
                continue
            seen.add(next)

            if valid_step(map, next):
                distances[next[0]][next[1]] = dist + 1

                paths.append((next, dist + 1))

seen = set()
cheats = {}

# def unitary_cheat(remaining, start, current, already_walked):
#     if remaining == 0:
#         return
#     
#     for dir in directions:
#         next = (current[0] + dir[0], current[1] + dir[1])
# 
#         print("unitary cheating", next, "remaining", remaining)
# 
#         if next[0] == 4 and next[1] == 7:
#             print("next:", next)
#             print("next:", next)
#             print("next:", next)
# 
#         if next == (4, 7):
#             print("next:", next)
# 
#         if next in seen:
#             continue
#         seen.add(next)
# 
#         if valid_cheat(map, next):
#             unitary_cheat(remaining - 1, start, next, already_walked + 1)
#         
#         if valid_step(map, next):
#             cheats[(start, next)] = already_walked + distances[next[0]][next[1]]
        
def unitary_cheat(start, walked):
    positions = collections.deque([(start, 20)])
    
    seen = set()
    seen.add(start)

    while len(positions) > 0:
        position = positions.popleft()
        current = position[0]
        to_walk = position[1]

        if valid_step(map, current) and to_walk != 20:
            cheats[(start, current)] = walked + (20-to_walk) + distances[current[0]][current[1]]

        if to_walk == 0:
            continue

        candidates = []
        for dir in directions:
            next = (current[0] + dir[0], current[1] + dir[1])

            if next in seen:
                continue
            seen.add(next)

            if valid_cheat(map, next):
                candidates.append((20-to_walk, next, to_walk-1))

        candidates = sorted(candidates)
        for candidate in candidates:
            positions.append((candidate[1], candidate[2]))

            

    # for dir in directions:
    #     next = (current[0] + dir[0], current[1] + dir[1])
# 
    #     print("unitary cheating", next, "remaining", remaining)
# 
    #     if next[0] == 4 and next[1] == 7:
    #         print("next:", next)
    #         print("next:", next)
    #         print("next:", next)
# 
    #     if next == (4, 7):
    #         print("next:", next)
# 
    #     if next in seen:
    #         continue
    #     seen.add(next)
# 
    #     if valid_cheat(map, next):
    #         unitary_cheat(remaining - 1, start, next, already_walked + 1)
    #     
    #     if valid_step(map, next):
    #         cheats[(start, next)] = already_walked + distances[next[0]][next[1]]

def cheat(start, already_walked):
    unitary_cheat(start, already_walked)
    # print(cheats)
    # for cheat, dist in cheats.items():
    #     if cheat[0] == (1,3) and cheat[1] == (4,7):
    #         print(cheat[0], cheat[1], dist)


def mega_cheat_search_dist(target_coordinate, best_path):
    valid_paths = []
    
    for steps, pos in enumerate(best_path):
        # seen = set()
        # print("cheating for pos", pos, steps)
        cheat(pos, steps)

        # todo remove
        # break

        # for dir in directions:
        #     for next_dir in directions:
        #         # if (dir, next_dir) in seen:
        #         #     continue
        #         # seen.add((dir, next_dir))
# 
        #         next = (pos[0] + dir[0], pos[1] + dir[1])
        #         next_next = (next[0] + next_dir[0], next[1] + next_dir[1])
# 
        #         if valid_cheat(map, next) and valid_step(map, next_next):
        #             if (next_next[0],next_next[1]) == target_coordinate:
        #                 valid_paths.append(steps + 2)
        #             else:
        #                 # print(next_next)
        #                 # TODO: Flood fill from the target to all valid positions
        #                 # to compute distances?
        #                 # _, _, remaining_to_end, _ = a_star(next_next, target_coordinate)
        #                 # print(current_path_len, remaining_to_end)
        #                 
        #                 remaining_to_end = distances[next_next[0]][next_next[1]]
        #                 full_steps = steps + remaining_to_end + 2
        #                 
        #                 valid_paths.append(full_steps)
# 
        #                 # paths = [(True, next_path)] + paths

    return valid_paths

distances = collections.defaultdict(lambda: collections.defaultdict(int))

def part1(input):
    for y, line in enumerate(input):
        line = line.replace('\n', '')
        if line != None:
            for x, char in enumerate(line):
                map[x][y] = char

                if char == "S":
                    start = (x, y)
                elif char == "E":
                    end = (x, y)

    width = len(map)
    height = len(map[0])
            
    # grid.display(map)

    # for y in range(height):
    #     for x in range(width):
    #         if map[x][y] != "#" and map[x][y] != "E":
    #             _, _, dist = a_star_dist(end, (x, y))
    #             print("(", x,", ", y, "):", dist)
    #             distances[x][y] = dist

    flood_dist(end)

    _, _, best_steps, best_path = a_star(start, end)
    
    count = 0
    gains = collections.defaultdict(int)
    cheat_path = cheat_search_dist(end, best_path)
    for steps in cheat_path:
        diff = best_steps - steps
        if diff > 0:
            gains[diff] += 1
            if diff >= 100:
                count += 1
        else:
            # TODO: optim here?
            # print("poor path")
            pass
     
    # 9464: too high
    # 1530
    return count

def part2(input):
    for y, line in enumerate(input):
        line = line.replace('\n', '')
        if line != None:
            for x, char in enumerate(line):
                map[x][y] = char

                if char == "S":
                    start = (x, y)
                elif char == "E":
                    end = (x, y)

    width = len(map)
    height = len(map[0])
            
    # grid.display(map)

    # for y in range(height):
    #     for x in range(width):
    #         if map[x][y] != "#" and map[x][y] != "E":
    #             _, _, dist = a_star_dist(end, (x, y))
    #             print("(", x,", ", y, "):", dist)
    #             distances[x][y] = dist

    flood_dist(end)

    _, _, best_steps, best_path = a_star(start, end)
    
    count = 0
    gains = collections.defaultdict(int)
    mega_cheat_search_dist(end, best_path)

    # print(len(cheats))
    # print(len(cheats))
    # print(len(cheats))

    for start_stop, saved in cheats.items():
        diff = best_steps - saved
        if diff > 0:
            if diff >= 100:
                gains[diff] += 1
                # print(start_stop, saved, diff)
                count += 1
            
    # print()
    # print()
    # print()
    # print(gains)


        # diff = best_steps - steps
        # if diff > 0:
        #     gains[diff] += 1
        #     if diff >= 50:
        #         count += 1
        # else:
        #     # TODO: optim here?
        #     # print("poor path")
        #     pass
     


    # 9464: too high
    # 1530
    return count

if __name__ == "__main__":
    main()
