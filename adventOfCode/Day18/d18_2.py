from collections import defaultdict
def getVal(inp, num):
    try:
        return int(inp)
    except:
        if num == 1:
            return regs_1[inp]
        else:
            return regs_2[inp]

with open('in.in','r') as f:
    data = f.readlines()

regs_1 = defaultdict(int)
i_1 = 0
regs_2 = defaultdict(int)
regs_2["p"] = 1
i_2 = 0
stuck_1 = False
stuck_2 = False
onetotwo = []
twotoone = []
count = 0
rcv_1 = 0
rcv_2 = 0
while not(stuck_1 and stuck_2):
    while not stuck_1: 
        instr = data[i_1]
        #print("1",i_1, instr)
        #print(regs_1, twotoone)
        ops = instr.split()
        if len(ops) == 2:
            op, arg1 = ops
        else:
            op, arg1, arg2 = ops
        if op == "set":
            regs_1[arg1] = getVal(arg2, 1)
        elif op == "snd":
            onetotwo.append(getVal(arg1, 1))
            stuck_2 = False
        elif op == "add":
            regs_1[arg1] += getVal(arg2, 1)
        elif op == "mul":
            regs_1[arg1] *= getVal(arg2, 1)
        elif op == "mod":
            regs_1[arg1] %= getVal(arg2, 1)
        elif op == "rcv":
            if len(twotoone) != 0:
                regs_1[arg1] = twotoone.pop(0)
                rcv_1 += 1
                #print("1", rcv_1)
            else:
                stuck_1 = True
                i_1 -= 1
        elif op == "jgz":
            if getVal(arg1, 1) > 0:
                i_1 += getVal(arg2, 1)
                i_1 -= 1
        i_1 += 1 

    while not stuck_2: 
        instr = data[i_2]
        print(regs_2, onetotwo)
        print("2", i_2, instr)
        
        ops = instr.split()
        if len(ops) == 2:
            op, arg1 = ops
        else:
            op, arg1, arg2 = ops
        if op == "set":
            regs_2[arg1] = getVal(arg2, 2)
        elif op == "snd":
            print("2", i_2, instr)
            count += 1
            #print(count)
            twotoone.append(getVal(arg1, 2))
            stuck_1 = False
        elif op == "add":
            regs_2[arg1] += getVal(arg2, 2)
        elif op == "mul":
            regs_2[arg1] *= getVal(arg2, 2)
        elif op == "mod":
            regs_2[arg1] %= getVal(arg2, 2)
        elif op == "rcv":
            if len(onetotwo) != 0:
                regs_2[arg1] = onetotwo.pop(0)
                rcv_2 += 1
                print("2", rcv_2)
            else:
                stuck_2 = True
                i_2 -= 1
        elif op == "jgz":
            if getVal(arg1, 2) > 0:
                i_2 += getVal(arg2, 2)
                i_2 -= 1
        i_2 += 1 
print(count)
