import collections
import hashlib

def main():
    print(part1("yzbqklnj"))
    print(part2("yzbqklnj"))

def part1(input):
    count = 0
    found = False

    while not found:
        count = count + 1
        test = input + str(count)
        result = hashlib.md5(bytes(test, "UTF-8")).hexdigest()

        if result.startswith("00000"):
            return count

def part2(input):
    count = 0
    found = False

    while not found:
        count = count + 1
        test = input + str(count)
        result = hashlib.md5(bytes(test, "UTF-8")).hexdigest()

        if result.startswith("000000"):
            return count

if __name__ == "__main__":
    main()