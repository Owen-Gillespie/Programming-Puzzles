from collections import Counter
def createTree(filename):
    with open(filename, 'r') as f:
        data = f.readlines()
    tower = {}
    for line in data:
        vals = line.replace(",","").split()
        name = vals[0]
        weight = int(vals[1][1:-1])
        if len(vals) > 2:
            children = vals[3:]
        else:
            children = []
        if name in tower:
            tower[name][0] = weight
            tower[name][1] = children
        else: 
            tower[name] = [weight, children, '']
        for child in children:
            if child in tower:
                tower[child][2] = name
            else:
                tower[child] = [0, [], name]
    return tower

def checkBalance(tower, root):
    children = tower[root][1]
    child_weights = [checkBalance(tower, child) for child in children]
    c = Counter(child_weights)
    if(len(c)) != 1 and len(c) != 0:
        bad_weight = c.most_common()[-1][0]
        good_weight = c.most_common()[0][0]
        bad_child = children[child_weights.index(bad_weight)]
        print(child + "should weigh " + str(tower[bad_child][0] + good_weight - bad_weight))
        # TODO: Restructure to avoid needing an Exception to stop
        raise Exception('Done') 
    return sum(child_weights) + tower[root][0]

def findRoot(tower):
    name = list(tower.keys())[0] # TODO: Find a better way to get arbitary key
    while tower[name][2] != '':
        name = tower[name][2]
    return name
#print(tower)
tree = createTree('input.txt')
root = findRoot(tree)
print("root: " + root)
checkBalance(tree, root)
