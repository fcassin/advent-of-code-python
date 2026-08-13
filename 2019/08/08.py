import collections
import math

from aoc import grid, ints, screen


TARGET = "input.txt"
WIDE = 25
TALL = 6


def main():
    with open(TARGET, "r") as input_file:
        print(part1(input_file.readlines()))

    with open(TARGET, "r") as input_file:
        print(part2(input_file.readlines()))


def parse(line):
    x, y = 0, 0
    layer = [[0] * WIDE for _ in range(TALL)]
    layers = list()

    for index, value in enumerate(ints.extract_contiguous(line)):
        x = index % WIDE
        y = index // WIDE % TALL

        if x == 0 and y == 0:
            if index != 0:
                layers.append(layer)
            layer = [[0] * WIDE for _ in range(TALL)]

        layer[y][x] = value

    layers.append(layer)
    return layers


def part1(input):
    result = 0

    for line in input:
        layers = parse(line)

        counts = {}
        for index, layer in enumerate(layers):
            count = collections.defaultdict(int)
            for line in layer:
                for value in line:
                    count[value] = count[value] + 1

            counts[index] = count

        lowest = math.inf
        for count in counts.values():
            if count[0] < lowest:
                lowest = count[0]
                result = count[1] * count[2]

    return result


def part2(input):
    for line in input:
        img = [[0] * TALL for _ in range(WIDE)]
        letters = [[" "] * TALL for _ in range(WIDE)]
        layers = parse(line)

        for x in range(WIDE):
            for y in range(TALL):
                for layer in layers:
                    if layer[y][x] in [0, 1]:
                        img[x][y] = layer[y][x]
                        if layer[y][x] == 1:
                            letters[x][y] = "#"
                        else:
                            letters[x][y] = "."

                        break

        return screen.read_letters_from_grid(letters)

    return 0


if __name__ == "__main__":
    main()
