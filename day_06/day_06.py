import os

from util import ROOT_DIR, read_lines

INPUT = read_lines(os.path.join(ROOT_DIR, 'day_06/day_06_input.txt'))


def get_orbit_dict(input_lines):
    orbit_dict = {}

    for line in input_lines:
        orbit, node = line.rstrip('\n').split(')')
        orbit_dict[node] = orbit

    return orbit_dict


def traverse(orbit_dict, current_node, count):
    # traverse until the node COM is found
    if current_node == 'COM':
        # print(current_node)
        return count
    else:
        count += 1
        # print(current_node, end='-->')
        return traverse(orbit_dict, orbit_dict[current_node], count)


def count_orbit_hops(orbit_dict):
    counts = []
    for key in orbit_dict.keys():
        counts.append(traverse(orbit_dict, key, 0))

    return sum(counts)


def solve_part_one(inputs):
    orbit_dict = get_orbit_dict(inputs)
    orbit_count = count_orbit_hops(orbit_dict)
    print(f'The total amount of orbit hops is {orbit_count}')
    return orbit_count


def solve_part_two(inputs):
    def plot_route(current_node, destination, route, count=0):
        route[current_node] = count
        if current_node == destination:
            return route
        else:
            count = count + 1
            return plot_route(orbit_dict[current_node], destination, route, count=count)

    orbit_dict = get_orbit_dict(inputs)
    # Exclude the first 'orbital hop' because the route is to the
    # object both YOU and SAN are orbiting, not from YOU to SAN
    start_san = orbit_dict['SAN']
    start_you = orbit_dict['YOU']
    route_you = plot_route(start_you, 'COM', route={})  # Route from YOU to COM
    route_san = plot_route(start_san, 'COM', route={})  # Route from SAN to COM
    matches = set([val for val in route_you.keys()]) & set([val for val in route_san.keys()])
    hop_count = {}

    for match in matches:
        hop_count[match] = route_you[match] + route_san[match]
    fastest_intersection = min(hop_count, key=hop_count.get)

    print(
        f'The fastest route is through {fastest_intersection}, this results in {hop_count[fastest_intersection]} hops'
    )
    return hop_count[fastest_intersection]


solve_part_one(INPUT)
solve_part_two(INPUT)
