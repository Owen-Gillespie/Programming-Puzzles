from math import sqrt

def partOne(instrs):
    regs = {x:0 for x in "abcdefgh"}
    count = 0
    i = 0
    while i < len(instrs):
        instr = instrs[i]
        op, arg1, arg2 = instr.split()
        if op == "set":
            regs[arg1] = getVal(arg2, regs)
        elif op == "sub":
            regs[arg1] -= getVal(arg2, regs)
        elif op == "mul":
            count += 1
            regs[arg1] *= getVal(arg2, regs)
        elif op == "jnz":
            if getVal(arg1, regs) != 0:
                i += getVal(arg2, regs)
                i -= 1
        i += 1
    return count

def getVal(arg, regs):
    try:
        return int(arg)
    except:
        return regs[arg]

def partTwo():
    '''This function was derived by inspecting the assembly code in 'in.in' and
        reverse engineering the code'''
    count = 0
    start = 107900
    for i in range(1001):
        if not prime(start):
            count += 1
        start += 17
    return count

def prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def d23(filename):
    with open(filename, 'r') as f:
        data = f.readlines()
    out1 = partOne(data)
    out2 = partTwo()
    return out1, out2

