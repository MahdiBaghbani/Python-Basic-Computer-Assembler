import argparse

from source.io_library import source_reader
from source.process import process


def main():
    parser = argparse.ArgumentParser(description='Morris Mano basic computer assembly compiler')
    parser.add_argument('-i', '--input', help='Input file path', required=True)
    parser.add_argument('-o', '--output', help='Output file path', required=True)
    args = parser.parse_args()
    source = source_reader(args.input)
    process(source)


if __name__ == '__main__':
    main()
