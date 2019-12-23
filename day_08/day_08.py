import os
from util import ROOT_DIR, read_file

INPUT_FILE = os.path.join(ROOT_DIR, 'day_08/day_08_input.txt')
DATA = [int(x) for x in read_file(INPUT_FILE)]
TEST_DATA = [int(x) for x in '123456789012']


class ImageProcessor:
    def __init__(self, width, height, data):
        self.width = width
        self.height = height
        self.data = data
        self.image = []

    def process(self):
        def chunks(lst, chunk_size):
            for x in range(0, len(lst), chunk_size):
                chunk = lst[x: x + chunk_size]
                yield chunk

        layer_buffer = []

        for chunk in chunks(self.data, self.width):
            layer_buffer.append(chunk)

            if len(layer_buffer) == self.height:
                self.image.append(layer_buffer)
                layer_buffer = []


def flatten_layer(layer):
    return [item for sublist in layer for item in sublist]


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


processor = ImageProcessor(25, 6, DATA)
processor.process()

print(solve_part_one(processor.image))
