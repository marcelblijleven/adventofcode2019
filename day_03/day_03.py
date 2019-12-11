import util
import os


root = os.path.dirname(os.path.abspath(__file__))


def get_movements(lines):
    wire_one = lines[0].split(',')
    wire_two = lines[1].split(',')
    return wire_one, wire_two


def move(movement, current_coord):
    coords = []
    direction = movement[0]
    steps = int(movement[1:])
    x, y = current_coord

    for step in range(steps):
        if direction == 'L':
            x += -1
        elif direction == 'D':
            y += -1
        if direction == 'R':
            x += 1
        elif direction == 'U':
            y += 1

        coords.append((x, y))

    return coords


def movements_to_coordinates(movements):
    coordinates = [(0, 0)]

    for movement in movements:
        coordinates += move(movement, coordinates[-1])

    return coordinates


def manhattan_distance(a, b):
    x1, y1 = a
    x2, y2 = b

    return abs(x1 - x2) + abs(y1 - y2)


def step_counter(wire_one, wire_two, intersections):
    pass



def execute(wire_one, wire_two):
    coords_one = movements_to_coordinates(wire_one)
    coords_two = movements_to_coordinates(wire_two)

    intersections = (set(coords_one) & set(coords_two))
    coords = [coord for coord in intersections if coord != (0, 0)]
    closest = min([manhattan_distance((0, 0), coord) for coord in coords])

    return closest


def execute_part_two(wire_one, wire_two):
    coords_one = movements_to_coordinates(wire_one)
    coords_two = movements_to_coordinates(wire_two)
    intersections = (set(coords_one) & set(coords_two))
    coords = set([coord for coord in intersections if coord != (0, 0)])

    results = {}

    for coord in coords:
        wire_one_steps = 0
        wire_two_steps = 0

        for a in coords_one:
            if a == coord:
                for b in coords_two:
                    if b == coord:
                        results[coord] = wire_one_steps + wire_two_steps
                        break

                    wire_two_steps += 1

            wire_one_steps += 1

    return min(results.values())


def solve_part_one():
    lines = util.read_lines(root + '/day_03_input.txt')
    wire_one, wire_two = get_movements(lines)
    distance = execute(wire_one, wire_two)
    print(f'Solution part one: distance {distance}')


def solve_part_two():
    lines = util.read_lines(root + '/day_03_input.txt')
    wire_one, wire_two = get_movements(lines)
    results = execute_part_two(wire_one, wire_two)
    print(f'Solution part two: {results}')


solve_part_one()
solve_part_two()
