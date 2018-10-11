from source.__config__ import MRI
from source.__config__ import NON_MRI
from source.__config__ import PREUDOMSTRUCTION


def assembler(source: str, symbols_address: dict):
    lines = source.split('\n')
    # Location Counter
    LC = 0
    obj_dict = dict()

    for line in lines:
        strings = line.split()
        switch = len(strings)
        word = strings[0]
        if switch == 1:
            if word == PREUDOMSTRUCTION[3]:
                break
            else:
                obj_dict[LC] = NON_MRI[strings[0]]
        elif switch == 2:
            if word == PREUDOMSTRUCTION[0]:
                LC = int(strings[1]) - 1
            else:
                if word in MRI:
                    obj_dict[LC] = _assemble(strings, symbols_address, 0, 0)
                elif word in PREUDOMSTRUCTION:
                    obj_dict[LC] = num_converter(word, strings[1])
        elif switch == 3:
            state = True
            if word[-1] == ',':
                a = 1
                b = 0
                if strings[1] in PREUDOMSTRUCTION[1:3]:
                    state = False
            else:
                a = 0
                b = 1
            if state:
                obj_dict[LC] = _assemble(strings, symbols_address, a, b)
            else:
                obj_dict[LC] = num_converter(word, strings[2])
        elif switch == 4:
            obj_dict[LC] = _assemble(strings, symbols_address, 1, 1)
        LC += 1

    return obj_dict


def _assemble(strings: list, symbols_address: dict, index1: int, index2: int):
    three_bit_part = symbols_address[strings[index1 + 1]]
    one_bit_part = MRI[strings[index1]][index2]
    assembled = one_bit_part + three_bit_part
    return hex(int(assembled, 16))


def num_converter(word: str, number: str):
    if word == PREUDOMSTRUCTION[1]:
        return hex(int(number, 16))
    else:
        return hex(int(number))
