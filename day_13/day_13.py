import os

from intcode import Intcode
from util import ROOT_DIR, get_list_from_file

INPUT = get_list_from_file(os.path.join(ROOT_DIR, 'day_13/day_13_input.txt'))


class ArcadeCabinet:
    def __init__(self, data, play_free=False):
        if play_free:
            data[0] = 2

        self.intcode = Intcode(memory=data, inputs=[])
        self.outputs = []
        self.blocks = {}

    @property
    def max_x(self):
        return max([i.x for i in self.outputs])

    @property
    def max_y(self):
        return max([i.y for i in self.outputs])

    @property
    def tiles(self):
        return {0: ' ', 1: '█', 2: '▒', 3: '▁', 4: '◯'}

    def process_data(self):
        score = 0
        paddle_x = None
        ball_x = None
        self.intcode.input_lambda = (
            lambda: (ball_x > paddle_x) - (ball_x < paddle_x)
        )

        while not self.intcode.halted:
            x = self.intcode.execute()
            y = self.intcode.execute()
            value = self.intcode.execute()
            self.outputs.append(value)

            if not self.intcode.halted:
                if value in self.tiles.keys():
                    self.blocks[(x, y)] = value

                if value == 3:
                    paddle_x = x
                elif value == 4:
                    ball_x = x
                elif x == -1 and y == 0:
                    score = value

        return score

    def count_tiles(self, tile_id):
        if len(self.outputs) == 0:
            self.process_data()

        return len([i for i in self.outputs if i == tile_id])


def solve_part_one():
    cabinet = ArcadeCabinet(INPUT)
    count = cabinet.count_tiles(tile_id=2)
    print('Number of block tiles:', count)


def solve_part_two():
    cabinet = ArcadeCabinet(INPUT, play_free=True)
    score = cabinet.process_data()
    print('Highscore:', score)



solve_part_one()
solve_part_two()