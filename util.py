import os, sys


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def read_lines(file):
    with open(file) as f:
        return f.readlines()


def get_list_from_file(file):
    with open(file) as f:
        content = f.read()
        lst = [int(item) for item in content.split(',')]
        return lst
