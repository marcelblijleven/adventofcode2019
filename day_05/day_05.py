import os

from intcode import Intcode
from util import ROOT_DIR, get_list_from_file

INPUT_FILE = os.path.join(ROOT_DIR, 'day_05/day_05_input.txt')
MEMORY = get_list_from_file(INPUT_FILE)


def solve_part_one():
    memory = MEMORY.copy()
    intcode = Intcode(memory, inputs=[1])
    output = intcode.execute()
    print(output)


def solve_part_two():
    memory = MEMORY.copy()
    intcode = Intcode(memory, inputs=[5])
    output = intcode.execute()
    print(output)


solve_part_one()
solve_part_two()
