def hexDistance(filename):
    with open(filename, 'r') as f:
        steps = f.read().rstrip().split(',')

    coords = [0,0,0]
    max_dist = 0
    # Find childs location in 'odd-q vertical layout'
    for step in steps:
        dx, dy, dz = takeStep(step, coords)
        coords[0] += dx
        coords[1] += dy
        coords[2] += dz
        max_dist = max(max_dist, distance(coords))
    return distance(coords), max_dist
def takeStep(step, coords):
    step_coords = {"n" : (0, 1, -1),
                "ne" : (1, 0, -1),
                "se" : (1, -1, 0),
                "s" : (0, -1, 1), 
                "sw" : (-1, 0 ,1),
                "nw" : (-1, 1, 0)}
    return step_coords[step]

def distance(coords):
    return sum([abs(x) for x in coords])//2

print(hexDistance('in.in'))
