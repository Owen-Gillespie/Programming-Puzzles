from collections import defaultdict

cache = defaultdict(int)
cache[(0,0)] = 1
def sumNeighbors(x,y):
    # TODO: Find a cleaner way to sum this
    val = cache[(x+1,y)] + cache[(x-1,y)] + cache[(x,y+1)] + cache[(x,y-1)] + cache[(x+1,y+1)] + cache[(x+1,y-1)] + cache[(x-1, y+1)] + cache[(x-1, y-1)]
    cache[(x,y)] = val
    print(x,y,val)
    return val

def walkSpiral(breakVal):
    walkLength = 1
    coords = [0,0]
    
    # TODO: make this into a function
    while True:
        # Walk right
        for i in range(walkLength):
            coords[0] += 1
            if sumNeighbors(coords[0], coords[1]) > breakVal:
                return sumNeighbors(coords[0], coords[1])
        # Walk up
        for i in range(walkLength):
            coords[1] += 1
            if sumNeighbors(coords[0], coords[1]) > breakVal:
                return sumNeighbors(coords[0], coords[1])

        walkLength += 1

        # Walk left
        for i in range(walkLength):
            coords[0] -= 1
            if sumNeighbors(coords[0], coords[1]) > breakVal:
                return sumNeighbors(coords[0], coords[1])

        # Walk down
        for i in range(walkLength):
            coords[1] -= 1
            if sumNeighbors(coords[0], coords[1]) > breakVal:
                return sumNeighbors(coords[0], coords[1])

        walkLength += 1



