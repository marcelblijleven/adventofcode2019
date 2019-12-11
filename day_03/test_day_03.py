import unittest

from day_03.day_03 import execute, execute_part_two, get_movements, move, manhattan_distance


class TestDay03(unittest.TestCase):
    def test_get_movements(self):
        lines = ['R75,D30,R83', 'U62,R66,U55']
        wire_one, wire_two = get_movements(lines)
        self.assertEqual(wire_one, ['R75', 'D30', 'R83'])
        self.assertEqual(wire_two, ['U62', 'R66', 'U55'])

    def test_manhattan_distance(self):
        distance = manhattan_distance((3, 5), (1, 6))
        self.assertEqual(distance, 3)

    def test_move(self):
        self.assertEqual(move('R2', (0, 0)), [(1, 0), (2, 0)])
        self.assertEqual(move('D2', (0, 0)), [(0, -1), (0, -2)])
        self.assertEqual(move('L2', (0, 0)), [(-1, 0), (-2, 0)])
        self.assertEqual(move('U2', (0, 0)), [(0, 1), (0, 2)])

    def test_execute_example_one(self):
        wire_one = 'R75,D30,R83,U83,L12,D49,R71,U7,L72'.split(',')
        wire_two = 'U62,R66,U55,R34,D71,R55,D58,R83'.split(',')
        self.assertEqual(execute(wire_one, wire_two), 159)

    def test_execute_example_two(self):
        wire_one = 'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51'.split(',')
        wire_two = 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'.split(',')
        self.assertEqual(execute(wire_one, wire_two), 135)

    def test_execute_example_one_part_two(self):
        wire_one = 'R75,D30,R83,U83,L12,D49,R71,U7,L72'.split(',')
        wire_two = 'U62,R66,U55,R34,D71,R55,D58,R83'.split(',')
        self.assertEqual(execute_part_two(wire_one, wire_two), 610)

    def test_execute_example_two_part_two(self):
        wire_one = 'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51'.split(',')
        wire_two = 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'.split(',')
        self.assertEqual(execute_part_two(wire_one, wire_two), 410)
