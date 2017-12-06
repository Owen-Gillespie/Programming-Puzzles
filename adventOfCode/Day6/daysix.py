def findCycle(filename):
    with open(filename, 'r') as f:
        str_cells = f.read().split()
    cells = [int(x) for x in str_cells]
    seen = dict()
    counter = 0
    while tuple(cells) not in seen:
        seen[tuple(cells)] = counter
        max_index = cells.index(max(cells))
        distributeBlocks(cells, max_index)
        counter += 1
    return len(seen), counter - seen[tuple(cells)]

def distributeBlocks(cells, max_index):
    max_val = cells[max_index]
    cells[max_index] = 0
    index = max_index
    for i in range(max_val):
        index = (index + 1) % len(cells)
        cells[index] += 1

