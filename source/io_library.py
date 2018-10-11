import os


def source_reader(path: str) -> str:
    """Reads source code
    :param path: string pointing to source code file location
    :return: source code
    """
    if not os.path.isfile(path):
        raise FileNotFoundError
    else:
        with open(path, 'r') as file:
            source = file.read()

    return source
