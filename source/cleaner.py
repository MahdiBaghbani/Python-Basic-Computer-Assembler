def cleaner(source: str):
    lines = source.split('\n')
    for i in range(len(lines)):
        strings = lines[i].split()
        for string in strings:
            if string[0] == ';':
                index = strings.index(string)
                delete = strings[index:]
                for item in delete:
                    strings.remove(item)
        lines[i] = ' '.join(strings)
    return '\n'.join(lines)
