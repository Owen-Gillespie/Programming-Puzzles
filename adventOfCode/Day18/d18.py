from collections import defaultdict, deque
def getVal(inpt, regs, pid=None):
    try:
        return int(inpt)
    except:
        if pid is not None:
            return regs[pid][inpt]
        else:
            return regs[inpt]
def d18(filename):
    with open(filename, 'r') as f:
        instructions = f.readlines()
    out1 = partOne(instructions)
    out2 = partTwo(instructions, 2)
    return out1,out2
def partOne(instructions):
    regs = defaultdict(int)
    sound = 0
    rcv = 0
    i = 0
    while i < len(instructions):
        instr = instructions[i]
        ops = instr.split()
        if len(ops) == 2:
            op, arg1 = ops
        else:
            op, arg1, arg2 = ops
        if op == "set":
            regs[arg1] = getVal(arg2, regs)
        elif op == "snd":
            sound = getVal(arg1, regs)
        elif op == "add":
            regs[arg1] += getVal(arg2, regs)
        elif op == "mul":
            regs[arg1] *= getVal(arg2, regs)
        elif op == "mod":
            regs[arg1] %= getVal(arg2, regs)
        elif op == "rcv":
            if getVal(arg1, regs) != 0:
                return sound
        elif op == "jgz":
            if getVal(arg1, regs) > 0:
                i += getVal(arg2, regs)
                i -= 1
        i += 1 

def partTwo(instructions, programs):
    regs = [defaultdict(int) for x in range(programs)]
    idxs = [0 for x in range(programs)]
    msgs = [deque() for x in range(programs)]
    stuck = [False for x in range(programs)]
    count = 0
    for x in range(programs):
        regs[x]["p"] = x
    
    while not all(stuck):
        for pid in range(programs):
            if not stuck[pid]:
                break
            if pid == programs - 1:
                raise Exception("Did not find unblocked program, but deadlock test failed")

        instr = instructions[idxs[pid]].rstrip()
        ops = instr.split()
        if len(ops) == 2:
            op, arg1 = ops
        else:
            op, arg1, arg2 = ops

        if op == "rcv":
            if len(msgs[pid]) == 0:
               stuck[pid] = True
            else:
                regs[pid][arg1] = msgs[pid].pop()
                idxs[pid] += 1
        elif op == "jgz":
            if getVal(arg1, regs, pid) > 0:
                idxs[pid] += getVal(arg2, regs, pid)         
            else:
                idxs[pid] += 1
        else:
            if op == "set":
                regs[pid][arg1] = getVal(arg2, regs, pid)
            elif op == "snd":
                for other_pid in range(programs):
                    if other_pid != pid:
                        msgs[other_pid].appendleft(getVal(arg1, regs, pid)) 
                        stuck[other_pid] = False
                        if pid == 1:
                            count += 1
            elif op == "add":
                regs[pid][arg1] += getVal(arg2, regs, pid)
            elif op == "mul":
                regs[pid][arg1] *= getVal(arg2, regs, pid)
            elif op == "mod":
                regs[pid][arg1] %= getVal(arg2, regs, pid)
            else:
                raise Exception("Unknown op code")
            
            idxs[pid] += 1
    return count

print(d18('in.in'))
