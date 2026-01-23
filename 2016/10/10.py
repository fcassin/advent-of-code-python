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

bots = {}
outputs = {}
manipulating_bot = None 

def main():
    with open("input.txt", "r") as input_file:
        print(part1(input_file.readlines()))

    with open("input.txt", "r") as input_file:
        print(part2(input_file.readlines()))
    
class Output:
    def __init__(self, id):
        self.id = id
        self.values = set()
        
    def give(self, value, bots=None, outputs=None):
        self.values.add(value)
        return False    
    
class Bot:
    def __init__(self, id, low, high, low_output=False, high_output=False):
        self.id = id
        self.low = low
        self.high = high
        self.low_output = low_output
        self.high_output = high_output
        self.values = set()
        
    def give(self, value):
        self.values.add(value)
        
        if len(self.values) > 2:
            raise Exception("Bot has more than 2 values")
        elif len(self.values) == 2:
            if min(self.values) == 17 and max(self.values) == 61:
                global manipulating_bot
                manipulating_bot = self.id
            return True
        
        return False
        
    def distribute(self, bots, outputs, low_recipient, high_recipient):
        low_value = min(self.values)
        high_value = max(self.values)
        
        should_redistribute = low_recipient.give(low_value)
        if should_redistribute:
            redistribute(low_recipient, bots, outputs)
        
        should_redistribute = high_recipient.give(high_value)
        if should_redistribute:
            redistribute(high_recipient, bots, outputs)
            
        self.values = set()
        
def redistribute(receiving, bots, outputs):
    receiving_low = bots.get(receiving.low)
    receiving_high = bots.get(receiving.high)
    
    if receiving.low_output:
        receiving_low = outputs.get(receiving.low)
    if receiving.high_output:
        receiving_high = outputs.get(receiving.high)
        
    receiving.distribute(bots, outputs, receiving_low, receiving_high)
    
def part1(input):    
    instructions = []
    
    for line in input:
        line = line.strip()
        
        values = ints.extract(line)
        if line.startswith("bot"):
            bot = Bot(values[0], values[1], values[2])
            
            components = line.split("to")
            if "output" in components[1]:
                bot.low_output = True
                
                if values[1] not in outputs:
                    outputs[values[1]] = Output(values[1])
            if "output" in components[2]:
                bot.high_output = True
                
                if values[2] not in outputs:
                    outputs[values[2]] = Output(values[2])
            
            bots[values[0]] = bot
        elif line.startswith("value"):
            instructions.append(values)
        
    for instruction in instructions:
        receiving = bots[instruction[1]]
        should_redistribute = receiving.give(instruction[0])
        
        if should_redistribute:
            redistribute(receiving, bots, outputs)      
            
    return manipulating_bot

def part2(input):
    return outputs[0].values.pop() * outputs[1].values.pop() * outputs[2].values.pop()

if __name__ == "__main__":
    main()