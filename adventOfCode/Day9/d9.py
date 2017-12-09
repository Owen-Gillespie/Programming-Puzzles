def calcGroupScore(filename):
    with open(filename, 'r') as f:
        stream = f.read()
    skip = False
    garbage = False
    depth = 0
    score = 0
    garbage_cnt = 0
    for char in stream:
        if skip:
            skip = False
            continue 
        if char == '!':
            skip = True
            continue
        if garbage:
            if char == '>':
                garbage = False
            else:
                garbage_cnt += 1
        else: 
            if char == '<':
                garbage = True
            elif char == '{':
                depth += 1
            elif char == '}':
                score += depth
                depth -= 1
    return score, garbage_cnt
