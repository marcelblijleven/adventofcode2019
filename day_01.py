import math
import unittest
import util


def calculate_fuel(mass):
    return math.floor(mass / 3) - 2


def calculate_additional_fuel(mass):
    total = 0

    while mass > 0:
        mass = calculate_fuel(mass)

        if mass < 0:
            return total

        total += mass

    return total


class TestDayOne(unittest.TestCase):
    def test_calculate_fuel(self):
        self.assertEqual(calculate_fuel(12), 2)
        self.assertEqual(calculate_fuel(14), 2)
        self.assertEqual(calculate_fuel(1969), 654)
        self.assertEqual(calculate_fuel(100756), 33583)

    def test_calculate_additional_fuel(self):
        self.assertEqual(calculate_additional_fuel(1969), 966)
        self.assertEqual(calculate_additional_fuel(100756), 50346)


def calculate_part_one():
    lines = util.read_lines('day_01_input.txt')

    total_fuel = 0

    for line in lines:
        mass = int(line)
        total_fuel += calculate_fuel(mass)

    return total_fuel


def calculate_part_two():
    lines = util.read_lines('day_01_input.txt')

    total_fuel = 0

    for line in lines:
        mass = int(line)
        total_fuel += calculate_additional_fuel(mass)

    return total_fuel

part_one = calculate_part_one()
part_two = calculate_part_two()

print('Part 1', part_one)
print('Part 2', part_two)
