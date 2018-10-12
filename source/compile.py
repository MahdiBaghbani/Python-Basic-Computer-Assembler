import struct

from source.io_library import output_writer


def compiler(object_dict: dict, output_path: str, mode: str):
    header_list = list(object_dict.keys())
    header_list.sort()
    for memory_location in header_list:
        integer = int(object_dict[memory_location], 16)
        object_dict[memory_location] = struct.pack('>i', integer)
    output_writer(output_path, header_list, object_dict, mode)
