import sys
sys.path.append("../../")

import collections
import functools
import graph
import ints
import itertools
import letter
import hashlib

def main():
    with open("input.txt", "r") as input_file:
        print(part1(input_file.readlines()))

    with open("input.txt", "r") as input_file:
        print(part2(input_file.readlines()))

def password(door):
    password = []

    for i in itertools.count():
        m = hashlib.md5()
        m.update((door + str(i)).encode('utf-8'))
        h = m.hexdigest()
        
        if h.startswith('00000'):
            password.append(h[5])
            
        if len(password) == 8:
            break

    return "".join(password)

def part1(input):
    for line in input:
        code = line.strip()    
        
    return password(code)

def better_password(door):
    password = [None] * 8
    filled = 0

    for i in itertools.count():
        m = hashlib.md5()
        m.update((door + str(i)).encode('utf-8'))
        h = m.hexdigest()
        
        if h.startswith('00000') and h[5] in '01234567' and password[int(h[5])] is None:
            filled += 1
            print(f"Found {filled}: {h}", h[5], h[6])
            password[int(h[5])] = h[6]
            
        if filled == 8:
            break

    return "".join(password)

def part2(input):
    for line in input:
        code = line.strip()    
        
    return better_password(code)

if __name__ == "__main__":
    main()