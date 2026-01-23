
import sys
sys.path.append("../../")

import collections
import copy
import functools
import graph
import grid
import itertools
import letter
import hashlib
import re
import z3

def main():
    with open("input.txt", "r") as input_file:
        lines = input_file.readlines()
        print(part1(lines))
        print(part2(lines))

def part1(input):
    count = 0

    left_vals = list()
    right_vals = list()
    line_in_block = 0

    for y, line in enumerate(input):
        line = line.replace('\n', '')

        

        if line != None:
            if line == "":
                line_in_block = 0
                left_vals.clear()
                right_vals.clear()
                continue
                #todo solve

            if line_in_block == 0 or line_in_block == 1:
                line_in_block += 1
                line = line.split(':')[1]

                left, right = line.split(",")
                left = int(left.split("+")[1])
                right = int(right.split("+")[1])

                left_vals.append(left)
                right_vals.append(right)

                continue

            if line_in_block == 2:
                line = line.split(':')[1]

                l, r = line.split(",")
                l = int(l.split("=")[1])
                r = int(r.split("=")[1])

                # [94, 22] [34, 67] 8400 5400
                a = z3.Int('a')
                b = z3.Int('b')

                solver = z3.Solver()

                solver.add(a <= 100, b <= 100, left_vals[0]*a + left_vals[1]*b == l, right_vals[0]*a + right_vals[1]*b == r)
                solver.check()
                try:

                    keys = solver.model()

                    x = int(keys[a].__str__())
                    y = int(keys[b].__str__())

                    

                    count += 3 * x + y
                except Exception as e:
                    print(e)
                    continue


            

    # >>> z3.solve(a <= 100, b <= 100, 94*a + 22*b == 8400, 34*a + 67*b == 5400)
    # [b = 40, a = 80]


    return count

def part2(input):
    count = 0

    left_vals = list()
    right_vals = list()
    line_in_block = 0

    for y, line in enumerate(input):
        line = line.replace('\n', '')

        

        if line != None:
            if line == "":
                line_in_block = 0
                left_vals.clear()
                right_vals.clear()
                continue
                #todo solve

            if line_in_block == 0 or line_in_block == 1:
                line_in_block += 1
                line = line.split(':')[1]

                left, right = line.split(",")
                left = int(left.split("+")[1])
                right = int(right.split("+")[1])

                left_vals.append(left)
                right_vals.append(right)

                continue

            if line_in_block == 2:
                line = line.split(':')[1]

                l, r = line.split(",")
                l = int(l.split("=")[1]) + 10000000000000
                r = int(r.split("=")[1]) + 10000000000000

                # [94, 22] [34, 67] 8400 5400
                a = z3.Int('a')
                b = z3.Int('b')

                solver = z3.Solver()

                solver.add(left_vals[0]*a + left_vals[1]*b == l, right_vals[0]*a + right_vals[1]*b == r)
                solver.check()
                try:

                    keys = solver.model()

                    x = int(keys[a].__str__())
                    y = int(keys[b].__str__())

                    

                    count += 3 * x + y
                except Exception as e:
                    print(e)
                    continue


            

    # >>> z3.solve(a <= 100, b <= 100, 94*a + 22*b == 8400, 34*a + 67*b == 5400)
    # [b = 40, a = 80]


    return count

if __name__ == "__main__":
    main()