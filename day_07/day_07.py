import os
from itertools import permutations
from intcode import Intcode
from util import ROOT_DIR, get_list_from_file

INPUT_FILE = os.path.join(ROOT_DIR, 'day_07/day_07_input.txt')
MEMORY = get_list_from_file(INPUT_FILE)


def phase_sequences(phases):
    """
    Get all permutations for the list of phases
    :param phases: list of int
    :return: list of int
    """
    return list(permutations(phases))


def calculate_outputs(sequences, memory):
    log = {}

    for sequence in sequences:
        output = 0
        for phase in sequence:
            output = Intcode(memory, inputs=[phase, output]).execute()

        log[sequence] = output
    return log


def get_max_output(output_log):
    max_key = max(output_log, key=output_log.get)
    return max_key, output_log[max_key]


def solve_part_one():
    sequences = phase_sequences(range(0, 5))
    output_log = calculate_outputs(sequences, MEMORY)
    sequence, max_output = get_max_output(output_log)
    print(f'Sequence {sequence} generates the most output at {max_output}')


def solve_part_two():
    sequences = phase_sequences(range(5, 10))
    output_log = calculate_outputs(sequences, MEMORY)
    sequence, max_output = get_max_output(output_log)
    print(f'Sequence {sequence} generates the most output at {max_output}')


TEST_INPUT = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
TEST_INPUT_2 = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]
TEST_SOLUTION = 139629729
TEST_SOLUTION_2 = 18216


def run_test(memory, sequence):
    output_log = calculate_feedback_outputs([sequence], memory)
    print(output_log)

solve_part_one()
#solve_part_two()
#run_test(TEST_INPUT, (9,8,7,6,5))
