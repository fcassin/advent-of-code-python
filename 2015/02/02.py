def main():
    with open("input.txt", "r") as input_file:
        print(part1(input_file))

    with open("input.txt", "r") as input_file:
        print(part2(input_file))
    
def part1(input):
    total = 0
    
    for line in input:
        line = line.replace("\n", "")
        
        l, w, h = map(int, line.split("x"))

        mini = min(l*w, min(w*h, h*l))
        wrap = 2*l*w + 2*w*h + 2*h*l

        total = total + mini + wrap

    return total

def part2(input):
    total = 0
    
    for line in input:
        line = line.replace("\n", "")
        
        l, w, h = map(int, line.split("x"))

        maxi = max(l, max(w, h))
        perim = ((l+w+h) - maxi)*2
        ribbon = l*w*h

        total = total + perim + ribbon

    return total

if __name__ == "__main__":
    main()