def d24(filename):
    with open(filename, 'r') as f:
        data = f.readlines()
    components = []
    for line in data:
        component = map(int,line.split('/'))
        components.append(component)
    return bridgeBuilder(components, 0, None), longBridgeBuilder(components, 0, None)[1]

# TODO: Combine duplicate functionality
def bridgeBuilder(components, ports, component):
    if component:
        components.remove(component)
    if len(components) == 0:
        return 0
    possible_components = [x for x in components if ports in x]
    if len(possible_components) == 0:
        return 0
    scores = [score(comp) + bridgeBuilder(list(components), otherPort(comp, ports), comp) for comp in components if ports in comp]
    return max(scores)

def longBridgeBuilder(components, ports, component):
    if component:
        components.remove(component)
    if len(components) == 0:
        return 0, 0
    possible_components = [x for x in components if ports in x]
    if len(possible_components) == 0:
        return 0, 0
    scores = []
    for comp in possible_components:
        length, points = longBridgeBuilder(list(components), otherPort(comp, ports), comp)
        points += score(comp)
        length += 1
        scores.append((length, points))
    return sorted(scores, reverse=True)[0]

def score(component):
    return sum(component)

def otherPort(component, port):
    if component[0] == port:
        return component[1]
    return component[0]

