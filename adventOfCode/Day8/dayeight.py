from collections import defaultdict
def processInstructions(filename):
    with open(filename,'r') as f:
        instructions = f.readlines()
    maxval = 0
    regs = defaultdict(int)
    for instruction in instructions:
        instruction = instruction.split()
        reg = instruction[0]
        inc =  1 if instruction[1] == 'inc' else -1
        amt = int(instruction[2])
        cond1 = instruction[4]
        cond2 = instruction[6]
        op = instruction[5]
        if eval(str(regs[reg]) + op + cond2):
            regs[reg] += inc * amt
            #if inc:
            #    regs[reg] = regs.get(reg,0) + amt
            #else:
            #    regs[reg] = regs.get(reg,0) - amt
            maxval = max(maxval, regs[reg]) 
    print(max(regs.values()))
    print(maxval) 

print(processInstructions('in.in'))
