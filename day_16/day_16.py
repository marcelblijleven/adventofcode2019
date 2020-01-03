import os
from util import ROOT_DIR, read_file

INPUT = read_file(os.path.join(ROOT_DIR, 'day_16/day_16_input.txt'))

base_offset = [0, 1, 0, -1]


def calculate_offset(n):
    return [x for x in base_offset for _ in range(n)]


def apply_offset(numbers):
    result = ''

    for i, _ in enumerate(numbers):
        offset = calculate_offset(i + 1) * int((len(numbers) / 3))
        offset.pop(0)  # Remove first in offset
        sub_result = 0
        for ni, numstr in enumerate(numbers):
            number = int(numstr)
            sub_result += number * offset[ni]

        result += str(abs(sub_result))[-1]

    return result


def solve_part_one():
    output = INPUT
    for phase in range(1, 101):
        output = apply_offset(output)
        print(f'Phase {phase}: {output[0:8]}')

    print(f'After 100 phases, the output is {output[0:8]}')


solve_part_one()
