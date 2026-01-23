import collections
import hashlib

def main():
    with open("input.txt", "r") as input_file:
        print(part1(input_file))

    with open("input.txt", "r") as input_file:
        print(part2(input_file))

def parse(input):
    if input.startswith("turn on"):
        command = "turn on"

    if input.startswith("turn off"):
        command = "turn off"

    if input.startswith("toggle"):
        command = "toggle"

    input = input[len(command):]
    input = input.replace("through", "")
    input = " ".join(input.split())

    (start, end) = input.split(" ")

    return (command, *map(int, start.split(",")), *map(int, end.split(",")))

def turnOn1(pos, startX, startY, endX, endY):
    for x in range(startX, endX + 1):
        for y in range(startY, endY + 1):
            pos[x][y] = 1

def turnOff1(pos, startX, startY, endX, endY):
    for x in range(startX, endX + 1):
        for y in range(startY, endY + 1):
            pos[x][y] = 0

def toggle1(pos, startX, startY, endX, endY):
    for x in range(startX, endX + 1):
        for y in range(startY, endY + 1):
            if pos[x][y] == 0:
                pos[x][y] = 1
            else:
                pos[x][y] = 0

def part1(input):
    count = 0

    pos = collections.defaultdict(lambda: collections.defaultdict(int))
    
    for line in input:
        line = line.replace("\n", "")

        command, startX, startY, endX, endY = parse(line)

        if command == "turn on":
            turnOn1(pos, startX, startY, endX, endY)
        elif command == "turn off":
            turnOff1(pos, startX, startY, endX, endY)
        elif command == "toggle":
            toggle1(pos, startX, startY, endX, endY)

    for x in range(0, 1000):
        for y in range(0, 1000):
            count = count + pos[x][y]

    return count

def turnOn2(pos, startX, startY, endX, endY):
    for x in range(startX, endX + 1):
        for y in range(startY, endY + 1):
            pos[x][y] = pos[x][y] + 1

def turnOff2(pos, startX, startY, endX, endY):
    for x in range(startX, endX + 1):
        for y in range(startY, endY + 1):
            if pos[x][y] > 0:
                pos[x][y] = pos[x][y] - 1

def toggle2(pos, startX, startY, endX, endY):
    for x in range(startX, endX + 1):
        for y in range(startY, endY + 1):
            pos[x][y] = pos[x][y] + 2

def part2(input):
    count = 0

    pos = collections.defaultdict(lambda: collections.defaultdict(int))
    
    for line in input:
        line = line.replace("\n", "")

        command, startX, startY, endX, endY = parse(line)

        if command == "turn on":
            turnOn2(pos, startX, startY, endX, endY)
        elif command == "turn off":
            turnOff2(pos, startX, startY, endX, endY)
        elif command == "toggle":
            toggle2(pos, startX, startY, endX, endY)

    for x in range(0, 1000):
        for y in range(0, 1000):
            count = count + pos[x][y]

    return count

if __name__ == "__main__":
    main()