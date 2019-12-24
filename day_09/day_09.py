import os
from intcode import Intcode
from util import ROOT_DIR, get_list_from_file

INPUT_FILE = os.path.join(ROOT_DIR, 'day_09/day_09_input.txt')
MEMORY = get_list_from_file(INPUT_FILE)


def solve_part_one():
    intcode = Intcode(memory=MEMORY, inputs=[])
    intcode.execute(1)
    print('Part one:', intcode.output)


def solve_part_two():
    intcode = Intcode(memory=MEMORY, inputs=[])
    intcode.execute(2)
    print('Part two:', intcode.output)


solve_part_one()
solve_part_two()
