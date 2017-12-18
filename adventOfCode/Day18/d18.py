from collections import defaultdict
def getVal(inp):
    try:
        return int(inp)
    except:
        return regs[inp]
with open('in.in','r') as f:
    data = f.readlines()

regs = defaultdict(int)
sound = 0
rcv = 0
i = 0
while i < len(data):
    instr = data[i]
    # print(i, instr)
    ops = instr.split()
    if len(ops) == 2:
        op, arg1 = ops
    else:
        op, arg1, arg2 = ops
    if op == "set":
        regs[arg1] = getVal(arg2)
    elif op == "snd":
        sound = getVal(arg1)
    elif op == "add":
        regs[arg1] += getVal(arg2)
    elif op == "mul":
        regs[arg1] *= getVal(arg2)
    elif op == "mod":
        regs[arg1] %= getVal(arg2)
    elif op == "rcv":
        if getVal(arg1) != 0:
            print(sound)
            break
    elif op == "jgz":
        if getVal(arg1) > 0:
            i += getVal(arg2)
            i -= 1
    i += 1 


