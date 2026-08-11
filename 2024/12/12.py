import collections
import copy
import functools
import itertools
import hashlib
import re

from aoc import graph, grid, letter


map = collections.defaultdict(lambda:collections.defaultdict(str))

def main():
    with open("input.txt", "r") as input_file:
        lines = input_file.readlines()
        print(part1(lines))
        print(part2(lines))

regions = []
seen = set()
map = collections.defaultdict(lambda:collections.defaultdict(str))

def walk_region(map, current, plant):
    region = set()
    neighbours = set()
    
    if current in seen:
        return 0, 0, region, neighbours
    
    seen.add(current)
    region.add(current)

    area = 1
    perimeter = 0

    new_area = 0
    new_perimeter = 0

    plant = map[current[0]][current[1]]

    width = len(map)
    height = len(map[0])

    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    for dir in directions:
        new_x = current[0] + dir[0] 
        new_y = current[1] + dir[1] 

        # print(new_x, new_y)

        if 0 <= new_x < width and 0 <= new_y < height:
            # print("neighbours")
            if map[new_x][new_y] == plant:
                new_area, new_perimeter, new_region, new_neighbours = walk_region(map, (new_x, new_y), plant)
                area += new_area
                perimeter += new_perimeter
                neighbours.update(new_neighbours)
                region.update(new_region)
            else:
                perimeter += 1
                neighbours.add((new_x, new_y))
        else:
            perimeter += 1
            neighbours.add((new_x, new_y))

    return area, perimeter, region, neighbours


def part1(input):
    count = 0

    for y, line in enumerate(input):
        line = line.replace('\n', '')
        if line != None:
            for x, char in enumerate(line):
                map[x][y] = char
                

    # grid.display(map)

    width = len(map)
    height = len(map[0])

    for x in range(width):
        for y in range(height):
            if (x, y) not in seen:
                plant = map[x][y]
                
                area, perimeter, _, _ = walk_region(map, (x, y), plant)

                count += area * perimeter

    return count

""" def count_sides(region):
    region_list = sorted(list(region))
    next_list = region_list[1:] + region_list[:1]

    vertices = set()
    start = [region_list[0]]

    print("region", region_list, next_list)

    sides = 0

    dir_index = 0
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    direction = directions[dir_index]

    start = region_list[0]
    for i, point in enumerate(region_list):
        next = next_list[i]
        print(i, point, next)

        if direction == (0, -1):
            if start[1] <= next[1]:
                continue
            else:
                sides += 1
                dir_index += 1
                direction = directions[dir_index % 4]
                start = next
                continue
        elif direction == (1, 0):
            if start[0] >= next[0]:
                continue
            else:
                sides += 1
                dir_index += 1
                direction = directions[dir_index % 4]
                start = next
                continue
        elif direction == (0, 1):
            if start[1] >= next[1]:
                continue
            else:
                sides += 1
                dir_index += 1
                direction = directions[dir_index % 4]
                start = next
                continue
        elif direction == (-1, 0):
            if start[0] <= next[0]:
                continue
            else:
                sides += 1
                dir_index += 1
                direction = directions[dir_index % 4]
                start = next
                continue
                
    print("sides", sides)
    print("sides", sides)
    print("sides", sides) """

def zoom(region):
    new_region = list()

    for point in region:
        new_region.append((point[0] * 2, point[1] * 2))
        new_region.append((point[0] * 2 + 1, point[1] * 2))
        new_region.append((point[0] * 2, point[1] * 2 + 1))
        new_region.append((point[0] * 2 + 1, point[1] * 2 + 1))

    new_region = sorted(new_region)
    return new_region

def turtle_sides(region):
    # print(region)
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    dir_index = 1
    
    region_list = sorted(list(region))
    current = region_list[0]

    seen = set()

    sides = 0
    while (current[0], current[1], dir_index % 4) not in seen:
        seen.add((current[0], current[1], dir_index % 4))

        # try to turn left if possible
        left = directions[(dir_index - 1) % 4]
        left_cell = (current[0] + left[0], current[1] + left[1])
        if left_cell in region:
            # print("turning left")
            sides += 1

            current = left_cell
            dir_index -= 1
            continue

        # go forward
        forward = directions[dir_index % 4]
        forward_cell = (current[0] + forward[0], current[1] + forward[1])
        if forward_cell in region:
            # print("forward")
            current = forward_cell
            continue

        # hit a wall, turn right
        right = directions[(dir_index + 1) % 4]
        right_cell = (current[0] + right[0], current[1] + right[1])
        if right_cell in region:
            # print("turning right")
            sides += 1

            current = right_cell
            dir_index += 1
            continue

    return sides

def corners(region):
    corner_candidates = set()

    for x, y in region:
        for cx, cy in [(x - 0.5, y - 0.5), (x + 0.5, y - 0.5), (x + 0.5, y + 0.5), (x - 0.5, y + 0.5)]:
            corner_candidates.add((cx, cy))

    corners = 0
    for cx, cy in corner_candidates:
        config = [(sx, sy) in region for sx, sy in [(cx - 0.5, cy - 0.5), (cx + 0.5, cy - 0.5), (cx + 0.5, cy + 0.5), (cx - 0.5, cy + 0.5)]]
        number = sum(config)

        if number == 1:
            corners += 1
        elif number == 2:
            if config == [True, False, True, False] or config == [False, True, False, True]:
                corners += 2
        elif number == 3:
            corners += 1
    
    return corners

def part2(input):
    count = 0

    for y, line in enumerate(input):
        line = line.replace('\n', '')
        if line != None:
            for x, char in enumerate(line):
                map[x][y] = char
                

    # grid.display(map)

    seen.clear()

    width = len(map)
    height = len(map[0])

    regions = {}
    neighbours = {}

    current_region = 0
    for x in range(width):
        for y in range(height):
            if (x, y) not in seen:
                plant = map[x][y]

                area, perimeter, region, neighbour = walk_region(map, (x, y), plant)
                # TODO: surrounded by looking at neighbours
                
                regions[current_region] = region
                neighbours[current_region] = neighbour
                current_region += 1

                # print("regions:", regions)
                # print("neighbours:", neighbours)

    for index, region in regions.items():
        area = len(region)
        zoomed_region = zoom(region)
        # sides = turtle_sides(zoomed_region)
        
        sides = corners(region)

        # print("region index:", index, "sides", sides, "area", area)
        count += area * sides

        """ current_neighbours = neighbours[index]
        # print(current_neighbours)

        outside = False
        neighbouring_regions = set()
        for neighbour in current_neighbours:
            if neighbour[0] < 0 or neighbour[0] >= width or neighbour[1] < 0 or neighbour[1] >= height:
                outside = True
                break

            for ir, region in regions.items():
                # print("region:", region)
                for point in region:
                    if point == neighbour:
                        neighbouring_regions.add(ir)
        # print("neighbouring_regions", neighbouring_regions)

        # print(neighbouring_regions)
        if len(neighbouring_regions) == 1 and not outside:
            # region is surrounded!
            count += len(regions[neighbouring_regions.pop()]) * sides """


    # 889950: too high
    # 882672: too high
    # 865662
    return count

if __name__ == "__main__":
    main()
