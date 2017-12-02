def contiguousMatchingSum(filename):
    '''Takes in a string of digits and returns the sum of the digits whose
        previous neighbor is equivalent'''
    with open(filename, 'r') as f:
        data = f.read().strip()
    
    return sum([int(data[i]) for i in range(len(data)) if data[i] == data[i-1]])

def halfwayMatchingSum(filename):
    '''Takes in a string of digits and returns the sum of the digits which
        match the digit halfway ahead of them in the list. (Consider the list to be
        circular)'''
    with open(filename, 'r') as f:
        data = f.read().strip()
    halfLen = len(data)//2
    return sum(2*[int(data[i]) for i in range(halfLen) if data[i] == data[i+halfLen]])


print(contiguousMatchingSum('input.txt'))
print(halfwayMatchingSum('input.txt'))
