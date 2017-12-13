def createFirewall(filename):
    with open(filename, 'r') as f:
        lines = [line.split(': ') for line in f.readlines()]
    firewall = {int(depth): int(rng) for depth, rng in lines}

    return firewall

def checkDelay(depth, rng, delay=0):
    return (depth + delay) % (2 * (rng - 1)) == 0

def partOne(filename):
    firewall = createFirewall(filename)
    severity = 0
    for depth, rng in firewall.items():
        # Scanner at top
        if checkDelay(depth, rng):
            severity += depth * rng

    return severity

def partTwo(filename):
    firewall = createFirewall(filename)
    delay = 0

    while any(checkDelay(depth, rng, delay) for depth,rng in firewall.items()):
        delay+=1
    return delay

print(partOne('in.in'))
print(partTwo('in.in'))
