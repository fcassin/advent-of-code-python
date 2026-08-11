from aoc import intcode


TARGET = "input.txt"


def determine(mem):
    noun, verb = 0, 0

    for verb in range(100):
        for noun in range(100):
            work_mem = mem[:]
            work_mem[1] = noun
            work_mem[2] = verb
            work_mem = intcode.execute(work_mem)

            if work_mem[0] == 19690720:
                return noun, verb

    return noun, verb


def main():
    with open(TARGET, "r") as input_file:
        print(part1(input_file.readlines()))

    with open(TARGET, "r") as input_file:
        print(part2(input_file.readlines()))


def part1(input):
    mem = []

    for line in input:
        line = line.strip()

        mem = [int(code) for code in line.split(",")]
        mem[1] = 12
        mem[2] = 2
        mem = intcode.execute(mem)

    return mem[0]


def part2(input):
    noun, verb = 0, 0
    mem = []

    for line in input:
        line = line.strip()

        mem = [int(code) for code in line.split(",")]
        noun, verb = determine(mem)

    return noun * 100 + verb


if __name__ == "__main__":
    main()
