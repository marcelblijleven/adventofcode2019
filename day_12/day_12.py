import os

from itertools import combinations
from util import ROOT_DIR, read_lines


INPUT = read_lines(os.path.join(ROOT_DIR, 'day_12/day_12_input.txt'))
TEST_INPUT = read_lines(os.path.join(ROOT_DIR, 'day_12/test_input.txt'))


class Moon:
    def __init__(self, x, y, z):
        self.position_x, self.position_y, self.position_z = x, y, z
        self.velocity_x, self.velocity_y, self.velocity_z = 0, 0, 0

    @property
    def potential_energy(self):
        return (
            abs(self.position_x) + abs(self.position_y) + abs(self.position_z)
        )

    @property
    def kinetic_energy(self):
        return (
            abs(self.velocity_x) + abs(self.velocity_y) + abs(self.velocity_z)
        )

    def apply_gravity(self, moon):
        xa, xb = self._check_axis(self.position_x, moon.position_x)
        ya, yb = self._check_axis(self.position_y, moon.position_y)
        za, zb = self._check_axis(self.position_z, moon.position_z)
        self.velocity_x += xa
        self.velocity_y += ya
        self.velocity_z += za
        moon.velocity_x += xb
        moon.velocity_y += yb
        moon.velocity_z += zb

    def apply_velocity(self):
        self.position_x += self.velocity_x
        self.position_y += self.velocity_y
        self.position_z += self.velocity_z

    def __str__(self):
        x, y, z = self.position_x, self.position_y, self.position_z
        vx, vy, vz = self.velocity_x, self.velocity_y, self.velocity_z
        return f'pos=<x={x}, y={y}, z={z}>, vel=<x={vx}, y={vy}, z={vz}>'

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

    def apply_velocity(self):
        for moon in self.moon_list:
            getattr(self, moon).apply_velocity()

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


# test()
solve_part_one()