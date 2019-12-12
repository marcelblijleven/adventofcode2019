import unittest

from day_04.day_04 import verify_number


class TestVerifyNumber(unittest.TestCase):
    def test_verify_number(self):
        self.assertEqual(verify_number(122345), True)
        self.assertEqual(verify_number(122045), False)

    def test_verify_number_with_adjacent_limit_E01(self):
        self.assertEqual(verify_number(112233, limit=True), True)

    def test_verify_number_with_adjacent_limit_E02(self):
        self.assertEqual(verify_number(123444, limit=True), False)

    def test_verify_number_with_adjacent_limit_E03(self):
        self.assertEqual(verify_number(111122, limit=True), True)
