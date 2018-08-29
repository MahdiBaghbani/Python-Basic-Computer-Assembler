import os
from precompile_library import precompile

MAX_LINE = 50


def source_reader(path: str):
    error_counter = 0
    line_number = 0
    source = list()
    declaration = list()
    usage = list()

    if not os.path.isfile(path):
        raise FileNotFoundError

    with open(path, 'r') as file:
        for line in file:
            error_counter += precompile(line, line_number, declaration, usage)
            source.append(line)
            line_number += 1
            if line_number > MAX_LINE:
                break
