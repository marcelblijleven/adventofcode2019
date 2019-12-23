import unittest


from intcode import process_instruction


class TestIntcode(unittest.TestCase):
    def test_get_parameter_modes(self):
        instruction_a = '00001'
        instruction_b = '00099'
        instruction_c = '01001'
        instruction_d = '01101'
        instruction_e = '00101'

        expected_a = (1, 0, 0, 0)
        expected_b = (99, 0, 0, 0)
        expected_c = (1, 0, 1, 0)
        expected_d = (1, 1, 1, 0)
        expected_e = (1, 1, 0, 0)

        self.assertEqual(process_instruction(instruction_a), expected_a)
        self.assertEqual(process_instruction(instruction_b), expected_b)
        self.assertEqual(process_instruction(instruction_c), expected_c)
        self.assertEqual(process_instruction(instruction_d), expected_d)
        self.assertEqual(process_instruction(instruction_e), expected_e)
