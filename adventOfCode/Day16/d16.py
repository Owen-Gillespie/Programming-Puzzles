from string import ascii_lowercase
from copy import deepcopy
NUM_PROGRAMS = 16
ALPHA_STRING = ascii_lowercase[:NUM_PROGRAMS]
BILLION = 10**9

def d16(filename):
    with open(filename, 'r') as f:
        instructions = f.read().split(',')
    out1 = partOne(instructions)
    out2 = partTwo(instructions)
    return out1, out2

def partOne(instructions):
    programs = list(ALPHA_STRING)
    programs = dance(instructions, programs)
    return "".join(programs)

def dance(instructions, programs):
    for instruction in instructions:
        programs = processInstruction(instruction, programs)
    return programs

def partTwo(instructions):
    programs = list(ALPHA_STRING)
    states = [list(ALPHA_STRING)]
    for i in xrange(BILLION): 
        programs = dance(instructions, programs)
        if programs == states[0]:
            return "".join(states[BILLION % (i + 1)])
        else:
            states.append(deepcopy(programs))

def processInstruction(instruction, programs):
    instr = instruction[0]
    if instr == "s":
        X = int(instruction[1:])
        programs = programs[-X:] + programs[:-X]
    else:
        if instr == "x":
            a, b = map(int, instruction[1:].split('/'))
        elif instr == "p":
            A, B = instruction[1:].split('/')
            a,b = programs.index(A), programs.index(B)
        programs[a], programs[b] = programs[b], programs[a]
    return programs
