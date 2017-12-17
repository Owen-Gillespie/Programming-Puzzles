def day17(step):
    buf = [0]
    index = 0
    for i in range(1, 2018):
        index = (index + step) % i + 1
        buf.insert(index, i)
    out1 =  buf[index + 1]
    for i in range(2018, 50000001):
        index = (index + step) % i + 1
        if index == 1:
            out2 = i
    return out1, out2 
