import sys
sys.path.append("../../")

import collections
import functools
import graph
import grid
import ints
import itertools
import letter
import hashlib
import screen

def main():
    with open("input.txt", "r") as input_file:
        print(part1(input_file.readlines()))

    with open("input.txt", "r") as input_file:
        print(part2(input_file.readlines()))
    
def part1(input):
    for line in input:
        line = line.strip()
        
        buffering = False
        
        parsing_window = False
        parsing_repeat = False
        
        window_buffer = ""
        repeat_buffer = ""
        
        result = ""
        buffer = ""
        
        window = 0
        repeat = 0
        
        for pos, char in enumerate(line):
            if char == '(' and not buffering:
                parsing_window = True
            elif char == 'x' and parsing_window and not buffering:
                parsing_window = False
                parsing_repeat = True    
            elif char == ')' and parsing_repeat and not buffering:
                buffer = ""
                buffering = True
                parsing_repeat = False
                
                window = int(window_buffer)
                repeat = int(repeat_buffer)
            elif parsing_window:
                window_buffer += char
            elif parsing_repeat:
                repeat_buffer += char
            elif buffering:
                buffer += char
                window -= 1
                
                if window == 0:
                    buffering = False
                    
                    for _ in range(repeat):
                        result += buffer[-len(buffer):]
                    
                    window_buffer = ""
                    repeat_buffer = ""
            else:
                result += char          
            
    return len(result)

def count_decoded(substring, marker):
    count = 0
    
    if '(' in substring:
        current_char = 0
        
        while current_char < len(substring):
            if substring[current_char] == '(':
                closing_index = substring.find(')', current_char)
                tuple = [int(value) for value in substring[current_char + 1:closing_index].split('x')]
                
                count += marker[1] * count_decoded(substring[closing_index + 1:closing_index + 1 + tuple[0]], tuple)
                
                current_char = closing_index + 1 + tuple[0]
            else:
                count += marker[1]
                
                current_char += 1
    else:
        return len(substring) * marker[1]
    
    return count

def part2(input):
    count = 0
    
    for line in input:
        line = line.strip()
    
        current_char = 0
        while current_char < len(line):
            if line[current_char] == '(':
                closing_index = line.find(')', current_char)
                tuple = [int(value) for value in line[current_char + 1:closing_index].split('x')]
                
                count += count_decoded(line[closing_index + 1:closing_index + 1 + tuple[0]], tuple)
                
                current_char = closing_index + 1 + tuple[0]
            else:
                count += 1
                
                current_char += 1
    return count            

if __name__ == "__main__":
    main()