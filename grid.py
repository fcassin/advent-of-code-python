import collections
import copy
import itertools
import png

DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# TODO: Update depth_first_search to match changes in breadth_first_search
# target should be switched to target_coordinate
# A mechanism to track shortest paths should be added
def depth_first_search(grid, valid_func, directions, starting_coordinate, target):
    valid_paths = []

    start = [starting_coordinate]
    paths = [start]

    while len(paths) > 0:
        path = paths.pop()
        current = path[len(path) - 1]

        for direction in directions:
            next = (current[0] + direction[0], current[1] + direction[1])

            if valid_func(grid, current, next):
                new_path = copy.deepcopy(path)
                new_path.append(next)

                if grid[next[0]][next[1]] == target:
                    valid_paths.append(new_path)
                else:
                    paths.append(new_path)

    return valid_paths

def default_directions(path):
    return DIRS

def breadth_first_search(grid, valid_func, dir_func, starting_coordinate, target_coordinate, memoize=True, max_steps=None):
    shortest_paths = {}
    valid_paths = []

    start = [starting_coordinate]
    paths = [start]

    while len(paths) > 0:
        path = paths.pop()
        current = path[len(path) - 1]
        
        if current == target_coordinate:
            continue
        
        if memoize:
            if current in shortest_paths:
                if len(path) > shortest_paths[current]:
                    continue
            shortest_paths[current] = len(path) - 1
        
        if max_steps is not None:
            if len(path) > max_steps:
                continue
        elif len(valid_paths) > 0 and len(path) > len(valid_paths[0]):
            continue

        for direction in dir_func(path):
            next = (current[0] + direction[0], current[1] + direction[1])

            if valid_func(grid, current, next):
                new_path = copy.deepcopy(path)
                new_path.append(next)

                if next == target_coordinate:
                    valid_paths.append(new_path)
                else:
                    paths = [new_path] + paths

    return (valid_paths, shortest_paths)

def default_validity_walled_grid(map, current, next):
    _ = current # Unused in this default implementation
    width = len(map)
    height = len(map[0])

    if next[0] >= 0 and next[0] < width and next[1] >= 0 and next[1] < height:
        if map[next[0]][next[1]] == "#":
            return False
        return True
        
    return False

def display(grid):
    cols = len(grid)
    rows = len(grid[0])

    for r in range(rows):
        for c in range(cols):
            print(grid[c][r], end="")
        print()

def to_png(grid, name):
    width = len(grid)
    height = len(grid[0])

    cols = []
    for y in range(height):
        row = []
        for x in range(width):
            if grid[x][y] == '.':
                row.append(0)
            else:
                row.append(255)

        cols.append(row)
    
    png.from_array(cols, mode="L").save("png/" + name + ".png")