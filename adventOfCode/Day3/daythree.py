from math import floor
def calculateCoords(index):
    '''Calculates the cartesian coordinates of an index in a spiral of natural
        number wrapping around 1 at coordinate (0,0)'''
    if index < 1:
        raise ValueError("must be a natural number")

    square_index = int(floor((index)**.5))
    if square_index % 2 == 0:
        square_coords = (-(square_index//2 - 1) , square_index//2)
    else:
        square_coords = ((square_index -1)//2, -(square_index-1)//2)
    x_offset, y_offset = offsetFromSquare(index,square_index)
    return (square_coords[0] + x_offset, square_coords[1] + y_offset)

def offsetFromSquare(index, root):
    square = root**2
    offset = index - square
    if offset == 0:
        return (0,0)
    mult = 1 if root % 2 == 1 else -1
    x_offset = -1 * max(-1, offset - root -2)
    y_offset = min(root, offset-1)
    return (mult * x_offset, mult * y_offset)


def distance(index):
    coords = calculateCoords(index)
    return abs(coords[0]) + abs(coords[1])

print(distance(312051))
