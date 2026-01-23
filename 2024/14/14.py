
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
import png
import re

map = collections.defaultdict(lambda:collections.defaultdict(str))

def main():
    with open("input.txt", "r") as input_file:
        lines = input_file.readlines()
        print(part1(lines))
        print(part2(lines))

robots = []
# width, height = 11, 7
width, height = 101, 103

def clear():
    for y in range(height):
        for x in range(width):
            map[x][y] = "."

def position():
    for robot in robots:
        p = robot[0]
        x, y = p

        # print("x, y:", x, y)

        if map[x][y] == '.':
            map[x][y] = '1'
        else:
            map[x][y] = str(int(map[x][y]) + 1)

def move():
    global robots

    clear()
    
    new_robots = []

    for robot in robots:
        p, v = robot[0], robot[1]
        x, y = p
        vx, vy = v

        xx = (x + vx) % width
        yy = (y + vy) % height

        # print("x, y:", x, y, "vx, vy:", vx, vy, "xx, yy:", xx, yy)

        if map[xx][yy] == '.':
            map[xx][yy] = '1'
        else:
            map[xx][yy] = str(int(map[xx][yy]) + 1)

        new_robots.append(((xx, yy), (vx, vy)))

    robots = new_robots

def part1(input):
    count = 0

    for y, line in enumerate(input):
        line = line.replace('\n', '')
        if line != None:
            p, v = line.split()
            x, y = (int(p) for p in p.split("=")[1].split(","))
            vx, vy = (int(v) for v in v.split("=")[1].split(","))

            # print(x, y, vx, vy)
            robots.append(((x,y), (vx,vy)))
    

    # print(robots)

    clear()
    position()
    # grid.display(map)

    for i in range(100):
        move()
    
    # grid.display(map)

    middle_width = (width + 1) // 2
    middle_height = (height + 1) // 2

    # print(middle_width, middle_height)

    top_left = 0
    for x in range(middle_width - 1):
        for y in range(middle_height - 1):
            if map[x][y] != '.':
                top_left += int(map[x][y])
    # print("top_left:", top_left)

    top_right = 0
    for x in range(middle_width, width):
        for y in range(middle_height - 1):
            if map[x][y] != '.':
                top_right += int(map[x][y])
    # print("top_right:", top_right)

    bottom_left = 0
    for x in range(middle_width - 1):
        for y in range(middle_height, height):
            if map[x][y] != '.':
                bottom_left += int(map[x][y])
    # print("bottom_left:", bottom_left)

    bottom_right = 0
    for x in range(middle_width, width):
        for y in range(middle_height, height):
            if map[x][y] != '.':
                bottom_right += int(map[x][y])
    # print("bottom_right:", bottom_right)

    return top_left * top_right * bottom_left * bottom_right

def part2(input):
    count = 0

    for y, line in enumerate(input):
        line = line.replace('\n', '')
        if line != None:
            p, v = line.split()
            x, y = (int(p) for p in p.split("=")[1].split(","))
            vx, vy = (int(v) for v in v.split("=")[1].split(","))

            robots.append(((x,y), (vx,vy)))
    

    # for i in range(width * height):
    #     move()
    #     grid.to_png(map, str(i + 1))

    return 7790

if __name__ == "__main__":
    main()