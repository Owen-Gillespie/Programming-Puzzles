DIRS = ["n", "e", "s", "w"]
def partOne(cells):
    pos = [len(cells[0])//2, len(cells)//2]
    dr = "n"
    count = 0
    for i in range(10000):
        #print(i, cells)
        if cells[pos[1]][pos[0]] == "#":
            dr = right(dr)
            cells[pos[1]] = cells[pos[1]][:pos[0]] + "." + cells[pos[1]][pos[0] + 1 :]
        else:
            dr = left(dr)
            cells[pos[1]] = cells[pos[1]][:pos[0]] + "#" + cells[pos[1]][pos[0] + 1 :]
            count += 1
        pos = forward(pos, dr) 
        if pos[0] < 0:
            cells = ["." * 10 + line for line in cells]
            pos[0] += 10
        if pos[0] >= len(cells[0]):
            cells = [line + "." * 10 for line in cells]
        if pos[1] < 0:
            cells = ["." * len(cells[0])] + cells
            pos[1] += 1
        if pos[1] >= len(cells):
            cells = cells + ["." * len(cells[0])] 
    return count
def left(dr):
    return DIRS[(DIRS.index(dr) - 1 ) % len(DIRS)]

def right(dr):
    return DIRS[(DIRS.index(dr) + 1 ) % len(DIRS)]
def forward(pos, dr):
    if dr == "w":
        return [pos[0] - 1, pos[1]]
    elif dr == "e":
        return [pos[0] + 1, pos[1]]
    elif dr == "n":
        return [pos[0], pos[1] - 1]
    elif dr == "s":
        return [pos[0], pos[1] + 1]
def partTwo(cells):
    pos = [len(cells[0])//2, len(cells)//2]
    dr = "n"
    count = 0
    for i in range(10000000):
        #print(i, cells)
        if cells[pos[1]][pos[0]] == "#":
            dr = right(dr)
            cells[pos[1]] = cells[pos[1]][:pos[0]] + "F" + cells[pos[1]][pos[0] + 1 :]
        elif cells[pos[1]][pos[0]] == "W":
            cells[pos[1]] = cells[pos[1]][:pos[0]] + "#" + cells[pos[1]][pos[0] + 1 :]
            count += 1
        elif cells[pos[1]][pos[0]] == ".":
            dr = left(dr)
            cells[pos[1]] = cells[pos[1]][:pos[0]] + "W" + cells[pos[1]][pos[0] + 1 :]
        elif cells[pos[1]][pos[0]] == "F":
            dr = left(left(dr))
            cells[pos[1]] = cells[pos[1]][:pos[0]] + "." + cells[pos[1]][pos[0] + 1 :]

        pos = forward(pos, dr) 
        if pos[0] < 0:
            cells = ["." * 10 + line for line in cells]
            pos[0] += 10
        if pos[0] >= len(cells[0]):
            cells = [line + "." * 10 for line in cells]
        if pos[1] < 0:
            cells = ["." * len(cells[0])] + cells
            pos[1] += 1
        if pos[1] >= len(cells):
            cells = cells + ["." * len(cells[0])] 
    return count
def d22(filename):
    with open(filename, 'r') as f:
        data = [x.rstrip() for x in f.readlines()]
    out1 = partOne(data)
    with open(filename, 'r') as f:
        data = [x.rstrip() for x in f.readlines()]
    out2 = partTwo(data)
    return out1, out2

#print(d22('test.in'))
print(d22('in.in'))
