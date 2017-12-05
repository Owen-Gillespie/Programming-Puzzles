def computeJumps(filename, partTwo):
    '''Takes in a file with a number on each line. The index starts pointing to
        the first line, and jumps forward by the number of lines of the value
        at the current index. After each jump, the value jumped from is
        incremented for part 1, and decremented if >=3, else incremented in
        part 2'''
    with open('input.txt', 'r') as f:
        str_jumps = f.readlines()
        jumps = [int(x) for x in str_jumps]

    counter = 0
    index = 0
    while 0 <= index < len(jumps):
        jump = jumps[index]
        if partTwo and jump >=3:
            jumps[index] -= 1
        else:
            jumps[index] += 1
        index += jump
        counter += 1
    print(counter)

