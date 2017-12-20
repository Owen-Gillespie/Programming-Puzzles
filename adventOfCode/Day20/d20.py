LONG_TERM_DIST = 10**9
MIN_STREAK = 1000

class Particle:
    def __init__(self, pos, vel, acc):
        self.pos = pos
        self.vel = vel
        self.acc = acc

    def x(self):
        return (pos[0], vel[0], acc[0])

    def y(self):
        return (pos[1], vel[1], acc[1])

    def z(self):
        return (pos[2], vel[2], acc[2])
    def incr(self):
        self.vel = [self.vel[i] + self.acc[i] for i in range(3)]
        self.pos = [self.pos[i] + self.vel[i] for i in range(3)]
        return tuple(self.pos)

    def __repr__(self):
        return "pos: " + str(self.pos) + " vel: " + str(self.vel) + " acc: " + str(self.acc)

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
    num_particles = len(coords)
    particles = {x[3]: Particle(x[0], x[1], x[2]) for x in coords}
    while streak < MIN_STREAK:
        current_pos = {}
        #print(current_pos)
        for i, particle in particles.items():
            pos = particle.incr()
            val = current_pos.get(pos,[])
            val.append(i)
            current_pos[pos] = val
        for key in current_pos.keys():
            if len(current_pos[key]) > 1:
                for prtcl_id in current_pos[key]:
                    del particles[prtcl_id]
        new_num_particles = len(particles)
        if new_num_particles == num_particles:
            streak += 1
        else:
            streak = 0
            num_particles = new_num_particles
    return num_particles

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
    out2 = partTwo(particle_coords)
    return out1, out2

def manhatten(coords):
    return sum(map(abs,coords))

def accelManhatten(coords):
    return manhatten(coords[2])
print(d20('in.in'))
