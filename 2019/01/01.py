TARGET = "input.txt"


def tyrannic_fuel(mass: int) -> int:
    if mass == 0:
        return 0

    return fuel(mass) + tyrannic_fuel(fuel(mass))


def fuel(mass: int) -> int:
    requirement = mass // 3 - 2

    if requirement < 0:
        requirement = 0

    return requirement


def main():
    with open(TARGET, "r") as input_file:
        print(part1(input_file.readlines()))

    with open(TARGET, "r") as input_file:
        print(part2(input_file.readlines()))


def part1(input):
    return sum([fuel(int(mass)) for mass in input])


def part2(input):
    return sum([tyrannic_fuel(int(mass)) for mass in input])


if __name__ == "__main__":
    main()
