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


def solve_part_one():
    output = INPUT
    for phase in range(1, 101):
        output = apply_offset(output)
        print(f'Phase {phase}: {output[0:8]}')

    print(f'After 100 phases, the output is {output[0:8]}')


# solve_part_one()


def get_multiplier(position, offset):
    base_pattern = [0, 1, 0, -1]
    if offset < position:
        return base_pattern[0]
    offset -= position
    return base_pattern[(offset // (position+1) + 1) % len(base_pattern)]

def part1(data):
    for _ in range(100):
        for i in range(len(data)):
            data[i] = abs(sum(data[j] * get_multiplier(i, j) for j in range(len(data)))) % 10
    return ''.join(map(str, data[:8]))

def part2(data):
    offset = int(''.join(map(str, data[:7])))
    data = (data*10000)[offset:]
    for _ in range(100):
        suffix_sum = 0
        for i in range(len(data)-1, -1, -1):
            data[i] = suffix_sum = (suffix_sum + data[i]) % 10
    return ''.join(map(str, data[:8]))

data = [int(x) for x in INPUT]
print('Part 1: {0}, Part 2: {1}'.format(part1(data[:]), part2(data[:])))
