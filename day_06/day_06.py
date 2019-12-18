import os

from util import ROOT_DIR, read_lines

INPUT = read_lines(os.path.join(ROOT_DIR, 'day_06/day_06_input.txt'))
TEST_INPUT = ['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L']


def get_orbit_dict(input_lines):
    orbit_dict = {}

    for line in input_lines:
        orbit, node = line.rstrip('\n').split(')')
        orbit_dict[node] = orbit

    return orbit_dict


def traverse(orbit_dict, current_node, count):
    # traverse until the node COM is found
    if current_node == 'COM':
        print(current_node)
        return count
    else:
        count += 1
        print(current_node, end='-->')
        return traverse(orbit_dict, orbit_dict[current_node], count)


def count_orbits(orbit_dict):
    counts = []
    for key in orbit_dict.keys():
        counts.append(traverse(orbit_dict, key, 0))

    return sum(counts)


def run_test(test_input):
    orbit_dict = get_orbit_dict(test_input)
    orbit_count = count_orbits(orbit_dict)
    assert orbit_count == 42

run_test(TEST_INPUT)


def solve_part_one(inputs):
    orbit_dict = get_orbit_dict(inputs)
    orbit_count = count_orbits(orbit_dict)
    print(orbit_count)
    return orbit_count


solve_part_one(INPUT)
