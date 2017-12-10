def partOne(filename, knot_len):
    with open(filename, 'r') as f:
        lengths = [int(x) for x in f.read().rstrip().split(',')]
    knot = [x for x in range(knot_len)]
    index = 0
    skip = 0
    knot = elfenTwisterRound(knot, lengths, index, skip, knot_len)[0]
    return knot[0] * knot[1]

def elfenTwisterRound(knot, lengths, index, skip, knot_len):
    for length in lengths:
        reverse(knot, length, index, knot_len)
        index = (index + length + skip) % knot_len
        skip += 1
    return knot, index, skip

def partTwo(filename, knot_len, num_rounds):
    with open(filename, 'r') as f:
        lengths = [ord(x) for x in f.read().rstrip()]
    lengths += [17, 31, 73, 47, 23]
    knot = [x for x in range(knot_len)]
    index = 0
    skip = 0
    for i_round in range(num_rounds):
        knot, index, skip = elfenTwisterRound(knot, lengths, index, skip,
                                              knot_len)
    hashes = [blockHash(knot[i:i+16]) for i in range(0, knot_len, 16)]
    return "".join(hashes) 

def reverse(knot, length, index, knot_len):
    if index + length <= knot_len:
        if index == 0:
            knot[index:index + length] = knot[index + length - 1:: -1]
        else:
            knot[index:index + length] = knot[index + length - 1: index - 1: -1]
    else:
        end = (index + length) % knot_len
        tail = knot[index:]
        head = knot[:end]
        for i, val in enumerate(tail + head):
            knot[end - i-1] = val

def blockHash(data):
    output = 0
    for datum in data:
        output = output ^ datum
    return "%0.2x" % output

# Example use
print(partOne('in.in', 256))
print(partTwo('in.in', 256, 64))
