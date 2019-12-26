import math
import os

from util import ROOT_DIR, read_lines

INPUT_FILE = os.path.join(ROOT_DIR, 'day_10/day_10_input.txt')


def get_asteroid_map():
    lines = read_lines(INPUT_FILE)
    # lines = TEST_INPUT.split('\n')[1:]
    asteroid_map = []

    # y is equal to number of lines
    for y in range(len(lines)):
        # x is equal to number of items in line
        for x in range(len(lines[y])):
            # check if position in lines is asteroid
            if lines[y][x] == '#':
                asteroid_map.append((x, y))

    return asteroid_map


def get_radian_angle(a, b):
    x1, y1 = a
    x2, y2 = b
    dx = x2 - x1
    dy = y2 - y1
    return math.atan2(dy, dx)


def radian_to_degrees(radian):
    return radian * (180 / math.pi) % 360


def correct_degrees(degrees):
    # Correct degrees to have upwards at 0 instead of 270
    degrees = degrees - 270 % 360

    if degrees < 0:
        return 360 + degrees
    else:
        return degrees


def calculate_distance(a, b):
    x1, y1 = a
    x2, y2 = b
    return math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))


def find_asteroid(asteroid_map):
    best_asteroid = None
    best_count = None

    for asteroid in asteroid_map:
        radian_set = set()
        for target_asteroid in asteroid_map:
            if target_asteroid == asteroid:
                continue

            radian = get_radian_angle(asteroid, target_asteroid)
            radian_set.add(radian)

        if best_count is None or len(radian_set) > best_count:
            best_count = len(radian_set)
            best_asteroid = asteroid
    # best_asteroid = (8, 3)  # REMOVE
    return best_asteroid, best_count


def get_asteroid_data(asteroid, asteroid_map):
    asteroid_data = {}

    for target_asteroid in asteroid_map:
        if target_asteroid == asteroid:
            continue

        radian = get_radian_angle(asteroid, target_asteroid)
        degrees = correct_degrees(radian_to_degrees(radian))
        distance = calculate_distance(asteroid, target_asteroid)

        try:
            asteroid_data[degrees].append((target_asteroid, distance))
        except KeyError:
            asteroid_data[degrees] = [(target_asteroid, distance)]

    # Sort all data by distance
    for value in asteroid_data.values():
        value.sort(key=lambda x: x[1])

    return asteroid_data


class AsteroidKillerBase:
    def __init__(self, position, asteroid_data):
        self.position = position
        self.asteroid_data = asteroid_data
        self.destroyed = []

    def execute(self):
        while len(self.destroyed) < 200:
            # Loop through sorted key, which equals degree
            for key in sorted(self.asteroid_data.keys()):
                if len(self.destroyed) == 200:
                    break

                self.destroyed.append(
                    self.asteroid_data[key].pop(0)[0]  # Return just the coords
                )

        return self.destroyed[199]


def solve_part_one():
    asteroid_map = get_asteroid_map()
    best_asteroid, best_count = find_asteroid(asteroid_map)
    print(
        f'Asteroid {best_asteroid} has {best_count} asteroids in direct sight.'
    )


def solve_part_two():
    asteroid_map = get_asteroid_map()
    best_asteroid, _ = find_asteroid(asteroid_map)
    asteroid_data = get_asteroid_data(best_asteroid, asteroid_map)
    asteroid_killer_base = AsteroidKillerBase(best_asteroid, asteroid_data)
    asteroid_200 = asteroid_killer_base.execute()
    result = asteroid_200[0] * 100 + asteroid_200[1]
    print(
        f'The 200th asteroid is located at {asteroid_200}. The result is {result}'
    )


solve_part_one()
solve_part_two()
