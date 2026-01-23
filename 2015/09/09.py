import sys
sys.path.append("../../")

import collections
import hashlib
import graph

def main():
    with open("input.txt", "r") as input_file:
        print(part1(input_file.readlines()))

    print(part2())

vertices = []
edges = []

def part1(input):
    for line in input:
        line = line.replace("\n", "")

        cities, weight = line.split(" = ")
        left, right = cities.split(" to ")

        if left not in vertices:
            vertices.append(left)

        if right not in vertices:
            vertices.append(right)

        edges.append((left, right, int(weight)))

    min_cost, _ = graph.travelling_salesman_no_return(vertices, edges)
    return min_cost

def part2():
    max_cost, _ = graph.travelling_showoff_no_return(vertices, edges)
    return max_cost


if __name__ == "__main__":
    main()