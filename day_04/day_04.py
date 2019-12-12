def verify_number(num):
    num_string = str(num)

    # It is a six digit number
    if len(num_string) != 6:
        return False

    has_adjacent = False

    # The digits never decrease
    # Two adjacent digits are the same
    for idx in range(5, -1, -1):
        if idx != 0 and int(num_string[idx]) < int(num_string[idx - 1]):
            return False

        if int(num_string[idx]) == int(num_string[idx - 1]) and not has_adjacent:
            has_adjacent = True

    return has_adjacent


def solve_part_one():
    results = []

    for num in range(356261, 846303):
        if verify_number(num):
            results.append(num)

    print(f'Solution part one: {len(results)}')


solve_part_one()