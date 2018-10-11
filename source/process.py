from source.analyzer import analyzer
from source.cleaner import cleaner
from source.precompile import precompile
from source.assembler import assembler


def process(source: str, output_file: str):
    source = cleaner(source)
    analyze(source)
    symbols_address = precompile(source)
    obj_dict = assembler(source, symbols_address)


def analyze(source: str):
    declaration = set()
    usage = set()
    error_counter = 0
    line_number = 1
    lines = source.split('\n')

    for line in lines:
        declaration, usage, err_c = analyzer(line, declaration, usage, line_number)
        error_counter += err_c
        line_number += 1

    if error_counter != 0:
        announce(error_counter)
    else:
        if declaration != usage:
            announce(1)


def announce(error_counter: int):
    print("Compiler found {} errors\nCompile FAILED\n".format(error_counter))
    exit(2)
