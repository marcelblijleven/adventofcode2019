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


def calculate_amplification_output(sequences, memory):
    log = {}

    for sequence in sequences:
        # Set initial output for first amplifier
        output = 0
        # Prepare intcode amplifiers
        intcode_amplifiers = [
            Intcode(memory=memory, inputs=[phase]) for phase in sequence
        ]

        # Loop until the last intcode amplifier halts
        while intcode_amplifiers[-1].halted is False:
            for intcode in intcode_amplifiers:
                output = intcode.execute(output)

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
    output_log = calculate_amplification_output(sequences, MEMORY)
    sequence, max_output = get_max_output(output_log)
    print(f'Sequence {sequence} generates the most output at {max_output}')


solve_part_one()
solve_part_two()

