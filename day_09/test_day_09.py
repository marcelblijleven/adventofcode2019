import unittest

from intcode import Intcode


class TestDay09(unittest.TestCase):
    def test_part_one_testcase1(self):
        memory = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
        expected_output = 109
        intcode = Intcode(memory=memory, inputs=[])
        intcode.execute()
        self.assertEqual(intcode.output, expected_output)

    def test_part_one_testcase2(self):
        memory = [1102,34915192,34915192,7,4,7,99,0]
        intcode = Intcode(memory=memory, inputs=[])
        intcode.execute()
        self.assertTrue(len(str(intcode.output)) == 16)

    def test_part_one_testcase3(self):
        memory = [104,1125899906842624,99]
        expected_output = 1125899906842624
        intcode = Intcode(memory=memory, inputs=[])
        intcode.execute()
        self.assertEqual(intcode.output, expected_output)
