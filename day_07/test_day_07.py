import unittest

from day_07.day_07 import phase_sequences


class TestDay07(unittest.TestCase):
    def test_phase_sequences(self):
        phases = range(0, 2)
        sequences = phase_sequences(phases)
        self.assertEqual(sequences, [(0, 1), (1, 0)])
