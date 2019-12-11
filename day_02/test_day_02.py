import unittest

from day_02 import process


class TestDayTwo(unittest.TestCase):
    def test_process(self):
        self.assertEqual(process([1, 0, 0, 0, 99], 0, 0), [2, 0, 0, 0, 99])
        self.assertEqual(process([2, 3, 0, 3, 99], 3, 0), [2, 3, 0, 6, 99])
        self.assertEqual(process([2, 4, 4, 5, 99, 0], 4, 4), [2, 4, 4, 5, 99, 9801])
        self.assertEqual(process([1, 1, 1, 4, 99, 5, 6, 0, 99], 1, 1), [30, 1, 1, 4, 2, 5, 6, 0, 99])
