import math
import os
import re

from collections import defaultdict, deque
from util import ROOT_DIR, read_lines


INPUT = read_lines(os.path.join(ROOT_DIR, 'day_14/day_14_input.txt'))
TEST_INPUT = [
    '9 ORE => 2 A', '8 ORE => 3 B', '7 ORE => 5 C',
    '3 A, 4 B => 1 AB', '5 B, 7 C => 1 BC', '4 C, 1 A => 1 CA',
    '2 AB, 3 BC, 4 CA => 1 FUEL'
]


class Chemical:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    @staticmethod
    def from_string(string):
        m = re.search('^(\d+) (\w+)', string)
        name = m.group(2)
        quantity = int(m.group(1))
        return Chemical(name, quantity)

    def __str__(self):
        return f'{self.quantity} {self.name}'

    def __repr__(self):
        return str(self)


class Reaction:
    def __init__(self, line):
        self.line = line
        self.inputs = []
        self.output = None
        self.process_line()

    def process_line(self):
        values = self.line.split(' => ')
        inputs, output = values[0], values[1]

        for i in inputs.split(', '):
            self.inputs.append(Chemical.from_string(i))

        self.output = Chemical.from_string(output)

    def __str__(self):
        return f'{[c for c in self.inputs]} will produce {self.output}'

    def __repr__(self):
        return str(self)


def get_reactions_from_input(data):
    return [Reaction(line) for line in data]


def find_reaction(name, reactions):
    for reaction in reactions:
        if reaction.output.name == name:
            return reaction

    print(f'No reaction found for chemical "{name}"')
    return None


def find_requirements(reactions, quantity=1):
    pantry = defaultdict(int)
    total_ore = 0
    requirements = deque()
    requirements.append(Chemical(name='FUEL', quantity=quantity))

    while len(requirements) != 0:
        requirement = requirements.popleft()

        # If requirement is ORE, no need to add to requirements
        # because ORE has no inputs
        if requirement.name == 'ORE':
            total_ore += requirement.quantity
        # If requirement is in the pantry, use that stock
        elif requirement.quantity <= pantry[requirement.name]:
            pantry[requirement.name] -= requirement.quantity
        else:
            reaction = find_reaction(requirement.name, reactions)
            needed = requirement.quantity - pantry[requirement.name]

            # Check if needed is more than the reaction supplies, if
            # that is the case, do the reaction n times until needed
            # is met. Add the remaining chemicals to the pantry
            n = math.ceil(needed / reaction.output.quantity)
            for _input in reaction.inputs:
                requirements.append(
                    Chemical(_input.name, _input.quantity * n)
                )

            pantry[requirement.name] = n * reaction.output.quantity - needed

    return total_ore


def solve_part_one():
    reactions = get_reactions_from_input(INPUT)
    ore = find_requirements(reactions)
    print('Total ore needed:', ore)


def solve_part_two():
    reactions = get_reactions_from_input(INPUT)
    # Got this from Excel, paste 1000000000000 and it
    # will say 1E+12 :)
    max_ore = int(1e12)
    min_ore = 10000
    ore_per_fuel = find_requirements(reactions, 1)
    estimated_ore = math.floor(max_ore / ore_per_fuel)

    while estimated_ore > min_ore:
        min_ore = estimated_ore
        ratio = find_requirements(reactions, min_ore)
        estimated_ore = math.floor(min_ore * max_ore) / ratio

    print('Amount of fuel', round(min_ore))


solve_part_one()
solve_part_two()
