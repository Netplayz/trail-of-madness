#!/usr/bin/env python3
import sys

def brainfuck_interpret(code, input_data=""):
    """Interpret and execute Brainfuck code"""
    memory = [0] * 30000
    pointer = 0
    output = []
    input_idx = 0
    pc = 0  # program counter
    
    # Find matching brackets
    bracket_map = {}
    bracket_stack = []
    for i, char in enumerate(code):
        if char == '[':
            bracket_stack.append(i)
        elif char == ']':
            if bracket_stack:
                start = bracket_stack.pop()
                bracket_map[start] = i
                bracket_map[i] = start
    
    while pc < len(code):
        instruction = code[pc]
        
        if instruction == '>':
            pointer += 1
            if pointer >= len(memory):
                memory.extend([0] * 1000)
        elif instruction == '<':
            pointer -= 1
        elif instruction == '+':
            memory[pointer] = (memory[pointer] + 1) % 256
        elif instruction == '-':
            memory[pointer] = (memory[pointer] - 1) % 256
        elif instruction == '.':
            output.append(chr(memory[pointer]))
        elif instruction == ',':
            if input_idx < len(input_data):
                memory[pointer] = ord(input_data[input_idx])
                input_idx += 1
        elif instruction == '[':
            if memory[pointer] == 0:
                pc = bracket_map.get(pc, pc)
        elif instruction == ']':
            if memory[pointer] != 0:
                pc = bracket_map.get(pc, pc)
        
        pc += 1
    
    return ''.join(output)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            code = f.read()
        result = brainfuck_interpret(code)
        print(result, end='')
    else:
        print("Usage: python3 bf_interpreter.py <brainfuck_file>")
