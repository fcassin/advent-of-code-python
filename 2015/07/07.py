import collections
import hashlib

def main():
    with open("input.txt", "r") as input_file:
        print(part1(input_file.readlines()))

    with open("input.txt", "r") as input_file:
        print(part2(input_file.readlines()))

def propagate(circuit, input):
    changes = 1

    while changes > 0:
        changes = 0

        for line in input:
            line = line.replace("\n", "")

            operation, wire = line.split(" -> ")

            # print(line, operation, wire)

            if wire not in circuit:
                if "AND" in operation:
                    left, right = operation.split(" AND ")
                    
                    if left in circuit and right in circuit:
                        changes = changes + 1
                        circuit[wire] = circuit[left] & circuit[right]

                elif "OR" in operation:
                    left, right = operation.split(" OR ")
                    
                    if left in circuit and right in circuit:
                        changes = changes + 1
                        circuit[wire] = circuit[left] | circuit[right]

                elif "NOT" in operation:
                    value = operation.replace("NOT ", "")
                    
                    if value in circuit:
                        changes = changes + 1
                        circuit[wire] = ~ circuit[value]

                elif "LSHIFT" in operation:
                    left, right = operation.split(" LSHIFT ")

                    if left in circuit:
                        changes = changes + 1
                        circuit[wire] = circuit[left] << int(right)

                elif "RSHIFT" in operation:
                    left, right = operation.split(" RSHIFT ")

                    if left in circuit:
                        changes = changes + 1
                        circuit[wire] = circuit[left] >> int(right)

                else:
                    if any(char.isdigit() for char in operation):
                        value = int(operation)

                        changes = changes + 1
                        circuit[wire] = value
                    else:
                        if operation in circuit:
                            changes = changes + 1
                            circuit[wire] = circuit[operation]

def part1(input):
    circuit = { "1": 1 }
    
    propagate(circuit, input)

    return circuit["a"]

def part2(input):
    circuit = { "1": 1 }
    
    propagate(circuit, input)

    aWire = circuit["a"]
    circuit = { "1": 1, "b": aWire }

    propagate(circuit, input)

    return circuit["a"]

if __name__ == "__main__":
    main()