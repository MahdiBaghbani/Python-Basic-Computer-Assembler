from source.analyzer import analyzer
from source.assembler import assembler
from source.cleaner import cleaner
from source.compile import compiler
from source.io_library import source_reader
from source.precompile import precompile


def process(input_file: str, output_file: str, mode: str):
    source = source_reader(input_file)
    source = cleaner(source)
    analyze(source)
    symbols_address = precompile(source)
    obj_dict = assembler(source, symbols_address)
    compiler(obj_dict, output_file, mode)
    print('\n Program compiled successfully!\n')


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
