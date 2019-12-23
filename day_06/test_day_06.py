import unittest

from day_06.day_06 import solve_part_one, solve_part_two


TEST_INPUT = ['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L']
TEST_INPUT_2 = ['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L', 'K)YOU', 'I)SAN']


class TestDay06(unittest.TestCase):
    def test_part_one(self):
        solution = solve_part_one(TEST_INPUT)
        self.assertEqual(solution, 42)

    def test_part_two(self):
        solution = solve_part_two(TEST_INPUT_2)
        self.assertEqual(solution, 4)
