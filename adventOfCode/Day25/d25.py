from collections import defaultdict
def d25(filename):
    with open(filename, 'r') as f:
        data = f.readlines()
    states = {}
    i = 0
    while i < len(data):
        line = data[i]
        line = line.rstrip().split()
        print(line)
        if len(line) > 0 and line[0] == "In": # New state declaration
            name = line[-1].strip(':')
            steps = [[0,0,0],[0,0,0]]
            steps[0][0] = int(data[i + 2][-3]) # Value to write
            steps[0][1] = data[i + 3].split()[-1] == "right." # Step direction
            steps[0][2] = data[i + 4][-3] # Next state
            steps[1][0] = int(data[i + 6][-3]) # Value to write
            steps[1][1] = data[i + 7].split()[-1] == "right." # Step direction
            steps[1][2] = data[i + 8][-3] # Next state
            states[name] = steps
            print(name, steps)
            i += 10
        else:
            i += 1
    tape = defaultdict(int)
    pos = 0
    cur_state = data[0][-3]
    num_steps = int(data[1].split()[-2])
    print(cur_state, num_steps)
    for i in xrange(num_steps):
        instr = states[cur_state][tape[pos]]
        tape[pos] = instr[0]
        if instr[1]:
            pos += 1
        else:
            pos -= 1
        cur_state = instr[2]
    return sum(tape.values())
print(d25('in.in'))
    
