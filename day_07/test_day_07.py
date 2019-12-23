import unittest

from day_07.day_07 import (
    phase_sequences, calculate_amplification_output, get_max_output
)


class TestDay07(unittest.TestCase):
    def test_phase_sequences(self):
        phases = range(0, 2)
        sequences = phase_sequences(phases)
        self.assertEqual(sequences, [(0, 1), (1, 0)])

    def test_part_two_testcase_a(self):
        sequences = [(9, 8, 7, 6, 5)]
        expected_max_output = 139629729
        memory = [
            3,26, 1001,26,-4,26, 3,27, 1002,27,2,27,
            1,27,26,27, 4,27, 1001,28,-1,28, 1005,28,6,
            99,0,0,5
        ]
        output_log = calculate_amplification_output(
            sequences, memory
        )

        sequence, max_output = get_max_output(output_log)
        self.assertEqual(expected_max_output, max_output)

    def test_part_two_testcase_b(self):
        sequences = [(9, 7, 8, 5, 6)]
        expected_max_output = 18216
        memory = [
            3,52,1001,52,-5,52,3,53,1,52,56,54,
            1007,54,5,55,1005,55,26,1001,54,-5,54,
            1105,1,12,1,53,54,53,1008,54,0,55,
            1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,
            1005,56,6,99,0,0,0,0,10
        ]
        output_log = calculate_amplification_output(
            sequences, memory
        )

        sequence, max_output = get_max_output(output_log)
        self.assertEqual(expected_max_output, max_output)

