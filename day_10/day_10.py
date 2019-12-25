import math
import os
from util import ROOT_DIR, read_lines

INPUT_FILE = os.path.join(ROOT_DIR, 'day_10/day_10_input.txt')


def get_asteroid_map():
    lines = read_lines(INPUT_FILE)
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


def find_asteroid(asteroid_map):
    best_asteroid = None
    best_count = None

    for asteroid in asteroid_map:
        radians_set = set()
        for target_asteroid in asteroid_map:
            if target_asteroid == asteroid:
                continue

            radians = get_radian_angle(asteroid, target_asteroid)
            radians_set.add(radians)

        if best_count is None or len(radians_set) > best_count:
            best_count = len(radians_set)
            best_asteroid = asteroid

    return best_asteroid, best_count


def solve_part_one():
    asteroid_map = get_asteroid_map()
    best_asteroid, best_count = find_asteroid(asteroid_map)
    print(f'Asteroid {best_asteroid} has {best_count} asteroids in direct sight.')


solve_part_one()