from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
LEFT = Point(-1, 0)
RIGHT = Point(1, 0)
UP = Point(0, 1)
DOWN = Point(0, -1)
PATH = []
DEBUG = False

def d19(filename):
    with open(filename, 'r') as f:
        pipes = f.readlines()
    out1,out2 = partOne(pipes)
    return out1, out2 

def partOne(pipes):
    for row in pipes:
        PATH.append([" " for x in row])
    height = len(pipes)
    width = len(pipes[0])
    j = 0
    output = ""
    steps = 0
    while pipes[0][j] != "|":
        j += 1
    x, y =  toCartesian(0, j, height)
    state = DOWN
    while 0 <= x <= width and 0 <= y <= height:
        x, y = x + state.x, y + state.y
        i, j = toListCoords(x, y, height)
        new_pipe = pipes[i][j]
        PATH[i][j] = new_pipe
        steps += 1
        if new_pipe not in "|-+":
            if new_pipe.isalpha():
                output += new_pipe
            else:
                prettyprint(PATH)
                return output, steps
        elif new_pipe == "+":
            state = findDirection(pipes, x, y, state)

def toCartesian(i, j, height):
    x = j 
    y = height - i
    return x, y

def toListCoords(x, y, height):
    i = height - y
    j = x
    return i, j

def prettyprint(PATH):
    if DEBUG:
        for row in PATH:
            print "".join(row)

def findDirection(pipes, x, y, state):
    if state.x == 0:
        # Currently up/down
        xl, yl = x + LEFT.x, y + LEFT.y
        il, jl = toListCoords(xl, yl, len(pipes))
        xr, yr = x + RIGHT.x, y + RIGHT.y
        ir, jr = toListCoords(xr, yr, len(pipes))
        if pipes[il][jl] == "-" or pipes[il][jl].isalpha():
            return LEFT
        elif pipes[ir][jr] == "-" or pipes[ir][jr].isalpha():
            return RIGHT
        else:
            prettyprint(PATH)
            raise Exception("Nowhere valid to go") 
    else:
        # Currently left/right 
        xu, yu = x + UP.x, y + UP.y
        iu, ju = toListCoords(xu, yu, len(pipes))
        xd, yd = x + DOWN.x, y + DOWN.y
        idwn, jd = toListCoords(xd, yd, len(pipes))
        if pipes[iu][ju] == "|" or pipes[iu][ju].isalpha():
            return UP 
        elif pipes[idwn][jd] == "|"or pipes[idwn][jd].isalpha():
            return DOWN 
        else:
            prettyprint(PATH)
            raise Exception("Nowhere valid to go")

print(d19('in.in'))
