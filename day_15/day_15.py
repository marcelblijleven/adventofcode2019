import os

from collections import deque
from copy import deepcopy
from enum import Enum
from intcode import Intcode
from util import ROOT_DIR, get_list_from_file


class Direction(Enum):
    North = 1
    South = 2
    West = 3
    East = 4


class Area(Enum):
    Wall = 0
    Open = 1
    Oxygen = 2


class Position:
    def __init__(self, x, y, steps):
        self.x = x
        self.y = y
        self.steps = steps

    @property
    def coordinates(self):
        return self.x, self.y

    def __add__(self, other):
        new_position = Position(self.x + other.x, self.y + other.y, self.steps)
        new_position.steps += 1  # No backtracking, so can safely add one step
        return new_position


INPUT = get_list_from_file(os.path.join(ROOT_DIR, 'day_15/day_15_input.txt'))
BLOCKS = ['█', '.', 'O']
DIRECTIONS = [
    (Direction.North, Position(0, -1, 1)),
    (Direction.South, Position(0, 1, 1)),
    (Direction.West, Position(-1, 0, 1)),
    (Direction.East, Position(1, 0, 1)),
]


class Droid:
    def __init__(self, intcode):
        self.position = Position(0, 0, 0)
        self.seen = {}
        self.queue = deque()
        self.map = {}
        self.oxygen_position = None

        # Provide initial values
        self.seen[self.position.coordinates] = intcode
        self.steps = {}
        self.queue.append(self.position)

    def plot_map(self):
        while self.queue:
            position = self.queue.pop()

            # For each direction, add possible positions to queue
            for direction, offset_position in DIRECTIONS:
                new_position = position + offset_position

                if new_position.coordinates not in self.seen:
                    intcode = deepcopy(self.seen[position.coordinates])
                    output = intcode.execute(direction.value)
                    self.steps[new_position.coordinates] = new_position.steps
                    self.seen[new_position.coordinates] = intcode
                    self.map[new_position.coordinates] = Area(output)

                    if output != 0:
                        if output == 2:
                            self.oxygen_position = new_position
                        # Add to queue
                        self.queue.appendleft(new_position)

    def find_route(self):
        if not self.oxygen_position:
            self.plot_map()

        return self.steps[self.oxygen_position.coordinates]

    def flood_room(self):
        if not self.oxygen_position:
            self.plot_map()
        time_passed = None

        flood_queue = [self.oxygen_position]
        seen = set()

        while flood_queue:
            next_queue = []
            while flood_queue:
                current_position = flood_queue.pop()
                current_coordinates = current_position.coordinates
                seen.add(current_coordinates)

                for _, offset_position in DIRECTIONS:
                    new_position = current_position + offset_position
                    new_coordinates = new_position.coordinates
                    if (
                        new_coordinates not in seen
                        and self.map.get(new_coordinates, Area.Wall) == Area.Open
                    ):
                        next_queue.append(new_position)

            flood_queue = next_queue
            time_passed = time_passed + 1 if time_passed is not None else 0
        return time_passed

    def print_map(self):
        min_y = min([key[1] for key in self.map.keys()])
        max_y = max([key[1] for key in self.map.keys()]) + 1
        min_x = min([key[0] for key in self.map.keys()])
        max_x = max([key[0] for key in self.map.keys()]) + 1

        for y in range(min_y, max_y):
            line = ''
            for x in range(min_x, max_x):
                if x == 0 and y == 0:
                    line += 'S'
                else:
                    area = self.map.get((x, y), Area.Wall)
                    line += BLOCKS[area.value]
            print(line)


def solve_part_one():
    intcode = Intcode(INPUT)
    droid = Droid(intcode)
    steps = droid.find_route()
    print(f'Fastest route to the oxygen tank takes {steps} steps.')


def solve_part_two():
    intcode = Intcode(INPUT)
    droid = Droid(intcode)
    time = droid.flood_room()
    print(f'The room was filled with oxygen in {time} minutes.')
    droid.print_map()

solve_part_two()