import math
import util


def calculate_fuel(mass):
    return math.floor(mass / 3) - 2


assert calculate_fuel(12) == 2
assert calculate_fuel(14) == 2
assert calculate_fuel(1969) == 654
assert calculate_fuel(100756) == 33583


def calculate_part_one():
    lines = util.read_lines('day_01_input.txt')

    total_fuel = 0

    for line in lines:
        mass = int(line)
        total_fuel += calculate_fuel(mass)

    return total_fuel
