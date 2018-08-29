import argparse


def main():
    parser = argparse.ArgumentParser(description='16-Bit CPU architecture assembly compiler')
    parser.add_argument('-i', '--input', help='Input file path', required=True)
    parser.add_argument('-o', '--output', help='Output file path', required=True)
    args = parser.parse_args()
