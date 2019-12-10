def read_lines(file):
    with open(file) as f:
        return f.readlines()


def get_list_from_file(file):
    with open(file) as f:
        content = f.read()
        lst = [int(num) for num in content.split(',')]
        return lst
