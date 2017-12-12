from collections import defaultdict, deque

def createGraph(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    graph = defaultdict(set)
    for line in lines:
        line = line.split()
        node = line[0]
        edges = "".join(line[2:]).split(',')
        graph[node].update(edges)
    return graph

def BFS(node, graph):
    q = deque()
    seen = set()
    q.appendleft(node)
    while len(q) != 0:
        cur_node = q.pop()
        seen.add(cur_node)
        for edge in graph[cur_node]:
            if edge not in seen:
                q.appendleft(edge)
    return seen

def countGroups(graph):
    to_visit = set(graph.keys())
    groups = 0
    while len(to_visit) > 0:
        groups += 1
        node = to_visit.pop()
        visited = BFS(node, graph)
        to_visit = to_visit - visited
    return groups

def partOne(filename):
    graph = createGraph(filename)
    return len(BFS('0', graph))

def partTwo(filename):
    graph = createGraph(filename)
    return countGroups(graph)

print(partOne('in.in'))
print(partTwo('in.in'))
