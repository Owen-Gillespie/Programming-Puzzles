LONG_TERM_DIST = 10**9
MIN_STREAK = 100
def partOne(coords):
    slowest_particles = sorted(coords, key=accelManhatten) 
    min_accel = accelManhatten(slowest_particles[0])
    for idx, particle in enumerate(slowest_particles):
        if accelManhatten(particle) > min_accel:
            break
    long_term_pos = []
    for particle in slowest_particles[:idx]:
        pos = [particle[0][i] + (particle[1][i] * LONG_TERM_DIST) + (particle[2][i] * LONG_TERM_DIST**2) for i in range(3)]
        long_term_pos.append(manhatten(pos))
    
    return slowest_particles[long_term_pos.index(min(long_term_pos))][3]

def partTwo(coords):
    streak = 0
    while streak < MIN_STREAK:
        current_pos = []
        for i in range(len(coords)):
            particle = coords[i]
           # TODO: Finish implementing simulator and add comments for part one 

def d20(filename):
    with open(filename, 'r') as f:
        particle_lines = f.readlines()
    particles = [line.split() for line in particle_lines] 
    particle_coords = []
    for i, particle in enumerate(particles):
        particle_coord = []
        for val in particle:
            coord = val[val.find("<")+1:val.find(">")].split(',')
            coord = map(int, coord)
            particle_coord.append(tuple(coord))
        particle_coords.append(tuple(particle_coord +[i]))
    out1 = partOne(particle_coords)
    return out1

def manhatten(coords):
    return sum(map(abs,coords))

def accelManhatten(coords):
    return manhatten(coords[2])
print(d20('in.in'))
