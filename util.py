import os, sys


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def read_file(file):
    with open(file) as f:
        return f.read()


def read_lines(file):
    with open(file) as f:
        return f.readlines()


def get_list_from_file(file):
    content = read_file(file)
    lst = [int(item) for item in content.split(',')]
    return lst


