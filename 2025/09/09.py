import sys
sys.path.append("../../")

import collections
import functools
import graph
import grid
import hashlib
import ints
import itertools
import letter
import math
import png
import screen

def main():
    with open("input.txt", "r") as input_file:
        print(part1(input_file.readlines()))

    with open("input.txt", "r") as input_file:
        print(part2(input_file.readlines()))
    
TILES = []
DISTANCES = []

LOW_X = 100000
LOW_Y = 100000

MAX_X = 0
MAX_Y = 0

TOP_LEFT = (1000000, 10000000)
    
def part1(input):
    global TILES
    global DISTANCES
    
    global LOW_X
    global LOW_Y
    
    global MAX_X
    global MAX_Y
    
    global TOP_LEFT
    
    for line in input:
        line = line.strip()
        
        coords = ints.extract(line)
        TILES.append( (coords[0], coords[1]) )
        
    # print(TILES)
    
    for x, first in enumerate(TILES):
        for y, second in enumerate(TILES):
            if x >= y:
                continue
            
            if first[0] > MAX_X:
                MAX_X = first[0]
            if second[0] > MAX_X:
                MAX_X = second[0]
                
            if first[1] > MAX_Y:
                MAX_Y = first[1]
            if second[1] > MAX_Y:
                MAX_Y = second[1]
                
            if first[0] < LOW_X:
                LOW_X = first[0]
            if second[0] < LOW_X:
                LOW_X = second[0]
                
            if first[1] < LOW_Y:
                LOW_Y = first[1]
            if second[1] < LOW_Y:
                LOW_Y = second[1]
                
            if first[1] < TOP_LEFT[1]:
                TOP_LEFT = first
            if second[1] < TOP_LEFT[1]:
                TOP_LEFT = second
                
            if first[1] == TOP_LEFT[1]:
                if first[0] < TOP_LEFT[0]:
                    TOP_LEFT = first
                    
            if second[1] == TOP_LEFT[1]:
                if second[0] < TOP_LEFT[0]:
                    TOP_LEFT = second
            
            distance = grid.manhattan(first, second)
            DISTANCES.append( (distance, x, y) )
    
    DISTANCES = sorted(DISTANCES, key=lambda x: x[0], reverse=True)
    # print(DISTANCES)
    
    longest = DISTANCES[0]
    
    a = TILES[longest[1]]
    b = TILES[longest[2]]
    
    # print(longest)
    first_side = abs(a[0] - b[0]) + 1
    second_side = abs(a[1] - b[1]) + 1
    
    # print(first_side, second_side)
            
    return first_side * second_side



def part2(input):
    global TILES

    # Build a smaller coordinate system
    xs = set()
    ys = set()
    for tile in TILES:
        xs.add(tile[0])
        ys.add(tile[1])
        
    xs = sorted(list(xs))
    ys = sorted(list(ys))
    
    smaller_tiles = []
    for tile in TILES:
        tile_index_x = xs.index(tile[0]) + 1
        tile_index_y = ys.index(tile[1]) + 1
        
        tile = (tile_index_x, tile_index_y)
        smaller_tiles.append(tile)
        
    map = collections.defaultdict(lambda: collections.defaultdict(lambda: '.'))
    
    for x in range(len(xs) + 2):
        for y in range(len(ys) + 2):
            map[x][y] = '.'
            
    for index, tile in enumerate(smaller_tiles):
        next = None
        if index == len(smaller_tiles) - 1:
            next = smaller_tiles[0]
        else:
            next = smaller_tiles[index + 1]
            
        if tile[0] == next[0]:
            # Vertical line
            low_y = min(tile[1], next[1])
            high_y = max(tile[1], next[1])
            
            for y in range(low_y, high_y + 1):
                map[tile[0]][y] = '#'
        elif tile[1] == next[1]:
            # Horizontal line
            low_x = min(tile[0], next[0])
            high_x = max(tile[0], next[0])
            
            for x in range(low_x, high_x + 1):
                map[x][tile[1]] = '#'
                
    grid.to_png(map, "part2-initial")
                
    # Flood fill from 0, 0
    queue = collections.deque()
    queue.append((0, 0))
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]    
    while len(queue) > 0:
        current = queue.popleft()
        
        for direction in directions:
            neighbor = (current[0] + direction[0], current[1] + direction[1])
            
            if neighbor[0] < 0 or neighbor[0] > len(xs) + 1 or neighbor[1] < 0 or neighbor[1] > len(ys) + 1:
                continue
            
            if map[neighbor[0]][neighbor[1]] == '.':
                map[neighbor[0]][neighbor[1]] = 'o'
                queue.append(neighbor)
    
    grid.to_png(map, "part2-floodfill")
    
    best_distance = 0
    for distance in DISTANCES:
        a = smaller_tiles[distance[1]]
        b = smaller_tiles[distance[2]]
        
        # Get rectangle corners
        x1 = a[0]
        y1 = a[1]
        
        x2 = b[0]
        y2 = b[1]
        
        low_x = min(x1, x2)
        high_x = max(x1, x2)
        
        low_y = min(y1, y2)
        high_y = max(y1, y2)
        
        # Check if we can draw the line
        can_draw = True
        for x in range(low_x, high_x + 1):
            for y in range(low_y, high_y + 1):
                if map[x][y] == 'o':
                    can_draw = False

        if can_draw:
            best_distance = distance
            break
        
    # Draw the best distance
    a = smaller_tiles[best_distance[1]]
    b = smaller_tiles[best_distance[2]]
    
    x1 = a[0]
    y1 = a[1]
    x2 = b[0]
    y2 = b[1]
    
    low_x = min(x1, x2)
    high_x = max(x1, x2)
    
    low_y = min(y1, y2)
    high_y = max(y1, y2)
    
    for x in range(low_x, high_x + 1):
        for y in range(low_y, high_y + 1):
            map[x][y] = 'x'
        
    grid.to_png(map, "part2-final")
    
    width = len(map)
    height = len(map[0])

    image = []
    for y in range(height):
        row = []
        for x in range(width):
            if map[x][y] == '.':
                row.extend([255, 0, 0])
            elif map[x][y] == 'o':
                row.extend([0, 0, 255])
            elif map[x][y] == 'x':
                row.extend([0, 255, 0])
            else:
                row.extend([255, 255, 255])

        image.append(row)
    
    print(image)
    
    png.from_array(image, mode="RGB").save("png/christmas_ornament.png")
        
    a = TILES[best_distance[1]]
    b = TILES[best_distance[2]]
    
    first_side = abs(a[0] - b[0]) + 1
    second_side = abs(a[1] - b[1]) + 1
    
    return first_side * second_side

if __name__ == "__main__":
    main()