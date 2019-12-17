import os

from intcode import Intcode
from util import ROOT_DIR, get_list_from_file

INPUT_FILE = os.path.join(ROOT_DIR, 'day_05/day_05_input.txt')
MEMORY = get_list_from_file(INPUT_FILE)


def solve_part_one():
    intcode = Intcode(MEMORY)
    output = intcode.execute()
    print(output)


solve_part_one()
