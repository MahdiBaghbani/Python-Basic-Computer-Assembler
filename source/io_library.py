import os
import struct


def source_reader(path: str) -> str:
    """ Reads source code

    :param path: string pointing to source code file location
    :return: source code
    """
    if not os.path.isfile(path):
        raise FileNotFoundError
    else:
        with open(path, 'r') as file:
            source = file.read()

    return source


def output_writer(path: str, header: list, object_dict: dict, mode: str):
    """ Writes compiled program

    :param path: output file path
    :param header: a list containing order of writing
    :param object_dict: dictionary containing bytes
    :param mode: switch between binary writing ('b') or textual writing ('t')
    """
    if mode == 'b':
        with open(path, 'wb+') as output:
            for memory_location in header:
                output.write(object_dict[memory_location])
    elif mode == 't':
        with open(path, 'w+') as output:
            for memory_location in header:
                integer = struct.unpack('>i', object_dict[memory_location])
                integer = integer[0]
                output.write(dec2bin(integer, 16) + '\n')


def dec2bin(decimal, bits) -> str:
    """ Converts a decimal number to it's 2nd complement binary representation

    :param decimal: decimal to be converted
    :param bits: number of bits for binary representation
    :return: string containing binary representation of decimal number
    """
    binary = bin(decimal & int("1" * bits, 2))[2:]
    return ("{0:0>%s}" % bits).format(binary)
