import collections
import contextlib
import functools
import hashlib
import itertools
import math
import sys
import time

from aoc import graph, grid, intcode, ints, letter, screen


TARGET = "input.txt"

FRAME_DELAY = 0.01


def main():
    with open(TARGET, "r") as input_file:
        print(part1(input_file.readlines()))

    with open(TARGET, "r") as input_file:
        print(part2(input_file.readlines()))


def part1(input):
    line = ints.extract(input[0].strip())

    vm = intcode.IntCodeVM("blocks")
    vm.memory(line)

    next(vm.run())

    blocks = {}
    while len(vm.outputs) > 0:
        x = vm.outputs.popleft()
        y = vm.outputs.popleft()
        b = vm.outputs.popleft()

        if b == 2:
            blocks[(x, y)] = b

    return len(blocks)


@contextlib.contextmanager
def animated():
    # Alternate screen buffer keeps the animation out of the scrollback, and the
    # finally clause makes sure the cursor comes back even on Ctrl-C.
    sys.stdout.write("\033[?1049h\033[?25l\033[2J")
    sys.stdout.flush()
    try:
        yield
    finally:
        # Clear before switching back: if the terminal ignores ?1049 the
        # animation was drawn on the normal buffer and would otherwise stay.
        sys.stdout.write("\033[2J\033[H\033[?25h\033[?1049l")
        sys.stdout.flush()


def draw(rows, score):
    frame = (
        "\033[H"
        + "".join("".join(row) + "\033[K\n" for row in rows)
        + f"score: {score}\033[K\n"
        + "\033[J"
    )
    sys.stdout.write(frame)
    sys.stdout.flush()


def part2(input):
    line = ints.extract(input[0].strip())

    vm = intcode.IntCodeVM("blocks")
    line[0] = 2
    vm.memory(line)

    graphics = {0: " ", 1: "#", 2: "X", 3: "_", 4: "O"}

    game = grid.infinigrid(" ")
    score = 0

    signal = None

    ball = (0, 0)
    paddle = (0, 0)

    with animated():
        while signal != intcode.Signal.HCF:
            for sig in vm.run():
                signal = sig

            while len(vm.outputs) > 0:
                x = vm.outputs.popleft()
                y = vm.outputs.popleft()
                b = vm.outputs.popleft()

                if x == -1 and y == 0:
                    score = b
                    continue

                game[x][y] = graphics[b]

                if b == 3:
                    paddle = (x, y)
                elif b == 4:
                    ball = (x, y)

            draw(grid.transpose(grid.materialize(game, fill=" ")), score)
            time.sleep(FRAME_DELAY)

            if ball[0] < paddle[0]:
                vm.input(-1)
            elif ball[0] > paddle[0]:
                vm.input(1)
            else:
                vm.input(0)

    return score


if __name__ == "__main__":
    main()
