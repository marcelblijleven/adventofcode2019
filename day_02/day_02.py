import util

from itertools import product


def process(memory, noun=None, verb=None):
    # Put noun at position 1, verb at position 2
    if noun is not None and verb is not None:
        memory[1] = noun
        memory[2] = verb

    def execute(start=0):
        step = 4
        opcode = memory[start]

        if opcode == 99 or start + step > len(memory):
            return memory

        param_one = memory[start + 1]
        param_two = memory[start + 2]
        destination = memory[start + 3]

        if opcode == 1:
            # Sum
            memory[destination] = memory[param_one] + memory[param_two]
        elif opcode == 2:
            # Multiply
            memory[destination] = memory[param_one] * memory[param_two]
        return execute(start + 4)

    return execute()


def solve_part_one():
    memory = util.get_list_from_file('day_02_input.txt')
    result = process(memory, 12, 2)
    print('Solution:', result[0])


def solve_part_two():
    memory = util.get_list_from_file('day_02_input.txt')
    expected = 19690720

    for noun, verb in product(range(100), repeat=2):
        mem_copy = memory.copy()
        result = process(mem_copy, noun, verb)[0]

        if result == expected:
            print('Solution:', 100 * noun + verb)
            break


solve_part_one()
solve_part_two()
