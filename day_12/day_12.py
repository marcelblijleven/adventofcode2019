import os

from itertools import combinations
from util import ROOT_DIR, read_lines


INPUT = read_lines(os.path.join(ROOT_DIR, 'day_12/day_12_input.txt'))
TEST_INPUT = read_lines(os.path.join(ROOT_DIR, 'day_12/test_input.txt'))


class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @property
    def energy(self):
        return abs(self.x) + abs(self.y) + abs(self.z)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __str__(self):
        return f'<x={self.x}, y={self.y}, z={self.z}>'


class Moon:
    def __init__(self, x, y, z):
        self.position = Vector(x, y, z)
        self.velocity = Vector(0, 0, 0)

    @property
    def potential_energy(self):
        return self.position.energy

    @property
    def kinetic_energy(self):
        return self.velocity.energy

    def apply_gravity(self, moon):
        xa, xb = self._check_axis(self.position.x, moon.position.x)
        ya, yb = self._check_axis(self.position.y, moon.position.y)
        za, zb = self._check_axis(self.position.z, moon.position.z)
        self.velocity += Vector(xa, ya, za)
        moon.velocity += Vector(xb, yb, zb)

    def apply_single_axis_gravity(self, moon, axis):
        if axis == 'x':
            a, b = self._check_axis(self.position.x, moon.position.x)
            self.velocity.x += a
            moon.velocity.x += b
        elif axis == 'y':
            a, b = self._check_axis(self.position.y, moon.position.y)
            self.velocity.y += a
            moon.velocity.y += b
        elif axis == 'z':
            a, b = self._check_axis(self.position.z, moon.position.z)
            self.velocity.z += a
            moon.velocity.z += b

    def apply_velocity(self):
        self.position += self.velocity

    def apply_single_axis_velocity(self, axis):
        if axis == 'x':
            self.position.x += self.velocity.x
        elif axis == 'y':
            self.position.y += self.velocity.y
        elif axis == 'z':
            self.position.z += self.velocity.z

    def __str__(self):
        return f'pos={self.position}, vel={self.velocity}'

    @staticmethod
    def _check_axis(a, b):
        if a < b:
            return 1, -1
        elif a > b:
            return -1, 1
        else:
            return 0, 0


class MoonMonitor:
    def __init__(self, input_lines):
        self.Io = Moon(*parse_moon_line(input_lines[0]))
        self.Europa = Moon(*parse_moon_line(input_lines[1]))
        self.Ganymede = Moon(*parse_moon_line(input_lines[2]))
        self.Callisto = Moon(*parse_moon_line(input_lines[3]))
        self.moon_list = ['Io', 'Europa', 'Ganymede', 'Callisto']

    @property
    def moon_pairs(self):
        return combinations(self.moon_list, 2)

    def apply_gravity(self):
        for pair in self.moon_pairs:
            name_a, name_b = pair
            moon_a = getattr(self, name_a)
            moon_b = getattr(self, name_b)
            moon_a.apply_gravity(moon_b)

    def apply_single_axis_gravity(self, axis):
        for pair in self.moon_pairs:
            name_a, name_b = pair
            moon_a = getattr(self, name_a)
            moon_b = getattr(self, name_b)
            moon_a.apply_single_axis_gravity(moon_b, axis)

    def apply_velocity(self):
        for moon_name in self.moon_list:
            getattr(self, moon_name).apply_velocity()

    def apply_single_axis_velocity(self, axis):
        for moon_name in self.moon_list:
            getattr(self, moon_name).apply_single_axis_velocity(axis)

    @property
    def total_energy(self):
        energy = 0
        for moon_name in self.moon_list:
            moon = getattr(self, moon_name)
            energy += moon.kinetic_energy * moon.potential_energy

        return energy

    def print_moons(self):
        for moon_name in self.moon_list:
            print(getattr(self, moon_name))


def gcd(a, b):
    return gcd(b, a % b) if b else a or 1


def lcm(a, b):
    return a * b // gcd(a, b)


def parse_moon_line(line):
    line = line.lstrip('<').rstrip('>\n')
    values = [int(val.split('=')[1]) for val in line.split(', ')]
    x, y, z = values
    return x, y, z


def test():
    monitor = MoonMonitor(TEST_INPUT)
    time = 0
    print(f'After {time} steps:')
    monitor.print_moons()

    while time < 10:
        time += 1
        monitor.apply_gravity()
        monitor.apply_velocity()
        print(f'After {time} steps:')
        monitor.print_moons()
        print(monitor.total_energy)
        print()


def solve_part_one():
    monitor = MoonMonitor(INPUT)
    time = 0

    while time < 1000:
        monitor.apply_gravity()
        monitor.apply_velocity()
        time += 1

    print(f'Total energy after 1000 steps: {monitor.total_energy}')


def solve_part_two():
    monitor = MoonMonitor(INPUT)

    # Calculate the period for each axis and each moon individually
    # this will return faster results than waiting for a period where
    # each axis is the same at the same time. Afterwards find the
    # least common multiple.
    # https://www.aa.quae.nl/en/reken/periode.html
    # https://en.wikipedia.org/wiki/Least_common_multiple
    moons = [getattr(monitor, name) for name in monitor.moon_list]
    seen_states = {'x': set(), 'y': set(), 'z': set()}
    steps = 1

    def get_axis(moon, axis):
        return getattr(moon.position, axis), getattr(moon.velocity, axis)

    def loop_axis(axis, moons):
        steps = 0
        while True:
            current_state = str([get_axis(moon, axis) for moon in moons])
            if current_state in seen_states[axis]:
                return steps
            else:
                seen_states[axis].add(current_state)
                monitor.apply_single_axis_gravity(axis)
                monitor.apply_single_axis_velocity(axis)
                steps += 1

    for axis in ['x', 'y', 'z']:
        axis_steps = loop_axis(axis, moons)
        print(f'Found {axis}: {axis_steps}')
        steps = lcm(steps, axis_steps)

    print(f'Returned to a previous state after {steps} steps')

# test()
solve_part_one()
solve_part_two()