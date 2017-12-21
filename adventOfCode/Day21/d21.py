def flip(image):
    return tuple([image[-i - 1] for i in range(len(image))])

def rotate(image):
    out = zip(*image[::-1])
    return tuple(["".join(x) for x in out])
with open('in.in', 'r') as f:
    data = f.readlines()
transforms = {}
for line in data:
    rule, output = line.rstrip().split(' => ')
    rule, output = rule.split('/'), output.split('/')
    transforms[tuple(rule)] = tuple(output)
image = [".#.", "..#", "###"]
size = 3
print(transforms) 
for k in range(18):
    print(k, size)
    if size % 2 == 0:
        print("upsize 2")
        outputs = []
        for m in range(size//2):
            for j in range(size//2):
                #print(image)
                inpt = [image[2 * m][2*j : 2 * j + 2], image[2 * m + 1][2 * j: 2*j + 2]]
                i = 0
                inpt = tuple(inpt)
                while inpt not in transforms:
                    #print(inpt)
                    if i > 16:
                        raise Exception("!")
                    if  i < 4 or i > 4:
                        inpt = rotate(inpt)
                        i += 1
                    if i == 4:
                        inpt = flip(inpt)
                        i += 1
                output = list(transforms[tuple(inpt)])
                outputs.append(output)
        total_output = ""
        for output in outputs:
            total_output+= "".join(output)
        size += size//2
        image = ["" for x in range(size)]
        for i, output in enumerate(outputs):
            #print(i, output)
            col = i // (size//3)
            for i in range(3):
                image[i + 3 * col] = image[i + 3 * col] + output[i]
        #print("output" + total_output)
        #image = [total_output[i * size: (i+1) * size] for i in range(size)]
        #print("output image: " + str(image))
    elif size % 3 == 0: 
        print("upsize 3")
        outputs = []
        for m in range(size//3):
            for j in range(size//3):
                #print(m,j, size//3)
                inpt = [image[3 * m][3*j : 3 * j + 3], image[3 * m + 1][3 * j: 3*j + 3], image[3 * m + 2][3*j: 3 * j + 3]]
                i = 0
                inpt = tuple(inpt)
                while inpt not in transforms:
                    #print(inpt)
                    if i > 16:
                        raise Exception("!")
                    if  i < 4 or i > 4:
                        inpt = rotate(inpt)
                        i += 1
                    if i == 4:
                        inpt = flip(inpt)
                        i += 1
                output = list(transforms[tuple(inpt)])
                outputs.append(output)
        total_output = ""
        size += size//3
        image = ["" for x in range(size)]
        for i, output in enumerate(outputs):
            #print(i, output)
            col = i // (size // 4)
            for i in range(4):
                image[i + 4 * col] = image[i + 4 * col] + output[i]
            #total_output+= "".join(output)
        #print("output" + total_output)
        #image = [total_output[i * size: (i+1) * size] for i in range(size)]
        #print("output image: " + str(image))
count = 0
for line in image:
    for char in line:
        if char == "#":
            count += 1
print("total on: " + str(count))
