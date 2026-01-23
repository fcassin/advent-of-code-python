def main():
    with open("input.txt", "r") as input_file:
        print(part1(input_file))

    with open("input.txt", "r") as input_file:
        print(part2(input_file))
            

def part1(input):
    left = 0
    right = 0

    for line in input:
        for char in line:
            if char == '(':
                left = left + 1
            elif char == ')':
                right = right + 1

    return left - right

def part2(input):
    position = 1

    for line in input:
        for count, char in enumerate(line):
            if char == '(':
                position = position + 1
            elif char == ')':
                position = position - 1
            
            if position == -1:
                return count

        return 0

if __name__ == "__main__":
    main()
