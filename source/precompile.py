from source.__config__ import PREUDOMSTRUCTION


def precompile(source: str):

    lines = source.split('\n')
    # Location Counter
    LC = 0
    symbols_address = dict()

    for line in lines:
        strings = line.split()
        if strings[0][-1] == ',':
            symbol = strings[0][:-1]
            symbols_address[symbol] = str(LC)
        elif strings[0] == PREUDOMSTRUCTION[0]:
            LC = int(strings[1]) - 1
        elif strings[0] == PREUDOMSTRUCTION[3]:
            break
        LC += 1

    return symbols_address
