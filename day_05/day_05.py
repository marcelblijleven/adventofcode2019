import os

from intcode import Intcode
from util import ROOT_DIR, get_list_from_file

input_file = os.path.join(ROOT_DIR, 'day_05/day_05_input.txt')
memory = get_list_from_file(input_file)

part_one, x = Intcode(memory, input_list=[1]).execute()

print(x)
