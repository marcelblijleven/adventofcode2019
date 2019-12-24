import os
from util import ROOT_DIR, read_file

INPUT_FILE = os.path.join(ROOT_DIR, 'day_08/day_08_input.txt')
DATA = [int(x) for x in read_file(INPUT_FILE)]


class ImageProcessor:
    def __init__(self, width, height, data):
        self.width = width
        self.height = height
        self.data = data
        self.raw_image = []
        self.image = []

    def process_data(self):
        layer_buffer = []

        for chunk in self._chunks(self.data, self.width):
            layer_buffer.append(chunk)

            if len(layer_buffer) == self.height:
                self.raw_image.append(layer_buffer)
                layer_buffer = []

    def decode_image(self):
        image_buffer = [['x' for _ in range(self.width)] for _ in range(self.height)]

        for layer in self.raw_image:
            for row_idx, row in enumerate(layer):
                for idx, pixel in enumerate(row):
                    if image_buffer[row_idx][idx] in ['x', 2]:
                        image_buffer[row_idx][idx] = pixel

        self.image = image_buffer

    def print_image(self):
        for row in self.image:
            row = [' ' if item == 0 else '█' for item in row]
            print(''.join(row))

    @staticmethod
    def _chunks(lst, chunk_size):
        for x in range(0, len(lst), chunk_size):
            chunk = lst[x: x + chunk_size]
            yield chunk


def flatten_layer(layer):
    return [item for sublayer in layer for item in sublayer]


def solve_part_one(image):
    target_layer = None
    target_count = None
    for layer in image:
        flattened = flatten_layer(layer)
        count = flattened.count(0)

        if target_count is None or target_count > count:
            target_count = count
            target_layer = flattened

    return target_layer.count(1) * target_layer.count(2)


def solve_part_two(processor):
    processor.decode_image()
    processor.print_image()


processor = ImageProcessor(25, 6, DATA)
processor.process_data()

print(solve_part_one(processor.raw_image))
solve_part_two(processor)
