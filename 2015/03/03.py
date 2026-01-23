import collections

def main():
    with open("input.txt", "r") as input_file:
        print(part1(input_file))

    with open("input.txt", "r") as input_file:
        print(part2(input_file))

def part1(input):
    pos = collections.defaultdict(lambda: collections.defaultdict(int))
    
    x = 0
    y = 0

    count = 1
    pos[x][y] = 1

    for line in input:
        for char in line:
            if char == "^":
                y = y + 1
            elif char == "v":
                y = y - 1
            elif char == "<":
                x = x - 1
            elif char == ">":
                x = x + 1

            if pos[x][y] == 0:
                count = count + 1

            pos[x][y] = pos[x][y] + 1
            

    return count

def part2(input):
    pos = collections.defaultdict(lambda: collections.defaultdict(int))
    
    xSanta = 0
    ySanta = 0
    xBot = 0
    yBot = 0

    count = 1
    pos[xSanta][ySanta] = 1

    for line in input:
        santa = True

        for char in line:
            if santa:
                santa = False
                
                if char == "^":
                    ySanta = ySanta + 1
                elif char == "v":
                    ySanta = ySanta - 1
                elif char == "<":
                    xSanta = xSanta - 1
                elif char == ">":
                    xSanta = xSanta + 1

                if pos[xSanta][ySanta] == 0:
                    count = count + 1

                pos[xSanta][ySanta] = pos[xSanta][ySanta] + 1
                
            else:
                santa = True

                if char == "^":
                    yBot = yBot + 1
                elif char == "v":
                    yBot = yBot - 1
                elif char == "<":
                    xBot = xBot - 1
                elif char == ">":
                    xBot = xBot + 1

                if pos[xBot][yBot] == 0:
                    count = count + 1

                pos[xBot][yBot] = pos[xBot][yBot] + 1

    return count

if __name__ == "__main__":
    main()