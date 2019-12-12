def verify_number(num, limit=False):
    num_string = str(num)

    # It is a six digit number
    if len(num_string) != 6:
        return False

    adjacent_monitor = {}

    # The digits never decrease
    # Two adjacent digits are the same
    for idx in range(5, -1, -1):
        if idx != 0 and int(num_string[idx]) < int(num_string[idx - 1]):
            return False

        if int(num_string[idx]) == int(num_string[idx - 1]):
            if num_string[idx] not in adjacent_monitor:
                adjacent_monitor[num_string[idx]] = 1
            else:
                adjacent_monitor[num_string[idx]] += 1

    if limit:
        return any([x == 1 for x in adjacent_monitor.values()])

    return any([x >= 1 for x in adjacent_monitor.values()])


def solve_part_one():
    results = []

    for num in range(356261, 846303):
        if verify_number(num):
            results.append(num)

    print(f'Solution part one: {len(results)}')


def solve_part_two():
    results = []

    for num in range(356261, 846303):
        if verify_number(num, limit=True):
            results.append(num)

    print(f'Solution part two: {len(results)}')


solve_part_one()
solve_part_two()
