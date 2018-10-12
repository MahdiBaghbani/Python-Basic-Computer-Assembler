import argparse

from source.process import process


def main():
    parser = argparse.ArgumentParser(description='Morris Mano basic computer assembly compiler')
    parser.add_argument('-i', '--input', help='Input file path', required=True)
    parser.add_argument('-o', '--output', help='Output file path', required=True)
    parser.add_argument('-m', '--mode', help='output format', default='t', required=False)
    args = parser.parse_args()
    process(args.input, args.output, args.mode)


if __name__ == '__main__':
    main()
