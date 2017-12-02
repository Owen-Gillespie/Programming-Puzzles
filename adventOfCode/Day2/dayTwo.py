def minMaxChecksum(filename):
    '''Reads in a file containing lines of numeric values seperated by
        whitespace.  Returns a 'checksum' found by summing the difference between the
        max and the min value in each row'''
    with open(filename, 'r') as f:
        lines = f.read().splitlines()

    rows = [convert(line) for line in lines]
    return sum([max(row) - min(row) for row in rows])

def divisionChecksum(filename):
    '''Reads in a file containing lines of numeric values seperated by
        whitespace.  Returns a 'checksum' found my summing the quotient of the only
        possible integer division with no remainder on each line'''
    with open(filename, 'r') as f:
        lines = f.read().splitlines()

    orderedRows = [sorted(convert(line)) for line in lines]
    return sum([findDivision(row) for row in orderedRows])

def convert(line):
    '''Splits on whitespace and casts strings to ints'''
    strRow = line.split()
    return [int(x) for x in strRow]


def findDivision(orderedRow):
    '''Takes in a sorted list (ascending) of ints and returns the quotient of
        the first successful integer division found or None if none are 
        found'''
    for i in range(len(orderedRow)):
        divisor = orderedRow[i]
        for dividend in orderedRow[i+1:]:
            if not(dividend % divisor):
                return dividend // divisor

