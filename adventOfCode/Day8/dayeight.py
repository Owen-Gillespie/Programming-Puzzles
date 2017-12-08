from collections import defaultdict
def processInstructions(filename):
    '''Takes in a file with instructions in the form
        'reg op value if reg comparison value'. Executes the operations and
        returns the maximum register value at the end of the program, and the maximum
        register value ever reached.  Registers default to a value of 0'''

    with open(filename,'r') as f:
        instructions = f.readlines()
    maxval = 0
    regs = defaultdict(int)
    for instruction in instructions:
        reg, cmd, amt, _, cond_reg, op, cond_val = instruction.split()
        inc =  1 if cmd == 'inc' else -1
        if eval(str(regs[cond_reg]) + op + cond_val):
            regs[reg] += inc * int(amt)
            maxval = max(maxval, regs[reg]) 
    return max(regs.values()), maxval 

print(processInstructions('in.in'))
