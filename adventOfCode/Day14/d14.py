from knothash import knotHash
def defrag(data, lines):
    free = 0
    memory = []
    for line in range(lines):
        hashed = knotHash(data + "-" + str(line))
        x = int(hashed, 16)
        binary = format(x, '0128b')
        # binary = "{0:b}".format(x)
        memory.append([x for x in binary])
        for char in binary:
            if char == "1":
                free += 1
    regions = 0
    # memory = [[c for c in word] for word in ["100","101","001"]]
    size = len(memory) - 1
    for i in range(128):
        for j in range(128):
            if memory[size - j][i] == "1":
                regions += 1
                exploreRegion(memory, i, j)
    return free, regions

def exploreRegion(grid, x, y):
    print(x,y)
    size = len(grid) - 1
    # print(grid)
    grid[size - y][x] = "0"
    # print(grid, size-y, x)
    # Check up
    if 0 <= (y + 1) <= size and grid[size - (y + 1)][x] == "1":
        exploreRegion(grid, x, y + 1)
    # Check Down
    if 0 <= (y - 1) >= 0 and grid[size - (y - 1)][x] == "1":
        exploreRegion(grid, x, y - 1)
    # Check Left 
    if x - 1 >= 0 and grid[size - y][x - 1] == "1":
        exploreRegion(grid, x - 1, y)
    # Check Right 
    if x + 1 <= size and grid[size - y][x + 1] == "1":
        exploreRegion(grid, x + 1, y)
    
print(defrag("wenycdww", 128))
