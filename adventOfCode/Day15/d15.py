FACTOR_A = 16807
FACTOR_B = 48271
MODULUS = 2147483647
MULT_A = 4
MULT_B = 8
MILLION = 10**6

def d15(start1, start2):
    return partOne(start1, start2), partTwo(start1, start2)

def genOne(start, factor):
    x = start
    while True:
        x = x * factor % MODULUS 
        yield format(x, '016b')

def genTwo(start, factor, multipleOf):
    x = start
    while True:
        x = (x * factor) % MODULUS 
        if x % multipleOf == 0:
            yield format(x, '016b')
            
def partOne(start1, start2):
    genA = genOne(start1, FACTOR_A)
    genB = genOne(start2, FACTOR_B)
    counter = 0
    for i in xrange(40 * MILLION):
        a,b = next(genA), next(genB)
        if a[-16:] == b[-16:]:
            counter += 1
    return counter

def partTwo(start1, start2):
    genA = genTwo(start1, FACTOR_A, MULT_A)
    genB = genTwo(start2, FACTOR_B, MULT_B)
    counter = 0
    for i in xrange(5 * MILLION):
        a,b = next(genA), next(genB)
        if a[-16:] == b[-16:]:
            counter += 1
    return counter

print(d15(634, 301))
