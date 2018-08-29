MAX_LINE = 50


def precompile(line: str, line_number: int, declaration: list, usage: list) -> int:
    mnemonics = ["AND", "ADD", "LDA", "STA", "BUN",
                 "BSA", "ISZ", "CLA", "CLE", "CMA",
                 "CME", "CIR", "CIL", "INC", "SPA",
                 "SNA", "SZA", "SZE", "HLT", "INP",
                 "OUT", "SKI", "SKO", "ION", "IOF",
                 "ORG", "DEC", "HEX", "END"]
    error_counter = 0

    line = line.split()
    words_number = len(line)

    if words_number == 1:
        pass
    elif words_number == 2:
        pass
    elif words_number == 3:
        pass
    elif words_number == 4:
        pass
    else:
        pass

    return error_counter


def show_error(error_code, line_number, error_counter):

    error_counter += 1

    if error_code == 1:
        print("\nERROR (line => {}): Exceeded max word in one line limit.\n".format(line_number))

    elif error_code == 2:
        print("\nERROR (line => {}): Only one word in one line is forbidden except END mnemonic.\n".format(line_number))

    elif error_code == 3:
        print(
            "\nERROR (line => {}): First character of variable/function/command can't be digits.\n".format(line_number))

    elif error_code == 4:
        print("\nERROR (line => {}): First element in this line of code should be finished with ','.\n".format(
            line_number))

    elif error_code == 5:
        print("\nERROR (line => {}): Last element in this line of code should be 'i'.\n".format(line_number))

    elif error_code == 6:
        print("\nERROR (line => {}): Can't recognize mnemonic\n".format(line_number))

    elif error_code == 7:
        print("\nERROR (line => {}): Using system reserved mnemonics for variable/function is forbidden. \n".format(
            line_number))

    elif error_code == 8:
        print("\nERROR (line => {}): UNRECOVERABLE ERROR: Invalid syntax.\n\nCOMPILE FAILED!\n".format(line_number))
        exit(1)

    elif error_code == 9:
        print("\nERROR (line => {}): The variable/function is not defined. \n".format(line_number))

    elif error_code == 10:
        print("\nERROR (line => {}): First element of line can't be only ','. \n".format(line_number))

    elif error_code == 11:
        print("\nERROR: Max line ({} lines) limit exceeded.\n", MAX_LINE)

    elif error_code == 12:
        print("\nERROR (line => {}): Variable/function name can't be more than 3 characters.\n".format(line_number))

    elif error_code == 13:
        print("\nERROR (line => {}): Hexadecimal number must be in range 0000 to FFFF.\n".format(line_number))

    elif error_code == 14:
        print("\nERROR (line => {}): Hexadecimal number should come after ORG/HEX mnemonic.\n".format(line_number))

    elif error_code == 15:
        print("\nERROR (line => {}): Decimal number must be 16-bit (in range 0 to 65536).\n".format(line_number))

    elif error_code == 16:
        print("\nERROR (line => {}): Decimal number should come after DEC mnemonic.\n".format(line_number))

    elif error_code == 17:
        print("\nERROR (line => {}): END mnemonic must be 1 word in one line.\n".format(line_number))

    else:
        print("\nINTERNAL ERROR: Invalid error code.")

    return error_counter
