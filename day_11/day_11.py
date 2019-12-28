import os

from intcode import Intcode
from util import ROOT_DIR, get_list_from_file

INPUT_FILE = os.path.join(ROOT_DIR, 'day_11/day_11_input.txt')
INPUT = get_list_from_file(INPUT_FILE)


class HullRobot:
    def __init__(self, data):
        self.x, self.y = 0, 0
        self.direction = 0  # Start facing upwards
        self.panels = {}
        self.intcode = Intcode(memory=data, inputs=[])

    def execute(self, initial_color=0):
        self.panels[self.position] = initial_color

        while self.intcode.halted is False:
            start_color = self.read_panel()
            next_color = self.intcode.execute(start_color)
            direction = self.intcode.execute()

            self.write_panel(next_color)
            self.rotate(direction)

        return self.panels

    @property
    def position(self):
        return self.x, self.y

    def read_panel(self):
        return (
            self.panels[self.position] if self.position in self.panels else 0
        )

    def write_panel(self, color):
        self.panels[self.position] = color

    def rotate(self, direction):
        # Rotate
        if direction == 0:
            self.direction = (self.direction - 90) % 360
        elif direction == 1:
            self.direction = (self.direction + 90) % 360

        # After rotating, move 1 panel
        if self.direction == 0:
            # Go up
            self.y += 1
        elif self.direction == 90:
            # Go right
            self.x += 1
        elif self.direction == 180:
            # Go down
            self.y -= 1
        elif self.direction == 270:
            # Go left
            self.x -= 1


def solve_part_one():
    robot = HullRobot(data=INPUT)
    panels = robot.execute()
    print(f'Number of panels painted at least once is {len(panels)}')


solve_part_one()
