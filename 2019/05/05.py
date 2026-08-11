from aoc import intcode


TARGET = "example.txt"


def main():
    # with open(TARGET, "r") as input_file:
    #    print(part1(input_file.readlines()))

    with open(TARGET, "r") as input_file:
        print(part2(input_file.readlines()))


def part1(input):
    mem = []
    out = []

    for line in input:
        line = line.strip()

        mem = [int(code) for code in line.split(",")]
        inp = [1]
        mem, out = intcode.execute(mem, inp)

    return out[-1]


def part2(input):
    mem = []
    out = []

    for line in input:
        line = line.strip()

        mem = [int(code) for code in line.split(",")]
        inp = [8]
        mem, out = intcode.execute(mem, inp)
        print(out)

    return out[-1]


if __name__ == "__main__":
    main()
