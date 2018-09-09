MAX_LINE = 50
NOTHING = 'NOTHING'


def preprocess(source: str):
    declaration = list()
    usage = list()
    error_counter = 0
    line_number = 1
    lines = source.split('\n')
    for line in lines:
        if line_number > MAX_LINE:
            error_counter += show_error(11, line_number)
            break
        declaration, usage, err_c = precompile(line, line_number, declaration, usage)
        error_counter += err_c
        line_number += 1


def precompile(line: str, line_number: int, declaration: list, usage: list) -> tuple:
    end = "END"
    mnemonics = ["AND", "ADD", "LDA", "STA", "BUN",
                 "BSA", "ISZ", "CLA", "CLE", "CMA",
                 "CME", "CIR", "CIL", "INC", "SPA",
                 "SNA", "SZA", "SZE", "HLT", "INP",
                 "OUT", "SKI", "SKO", "ION", "IOF",
                 "ORG", "DEC", "HEX", end]
    exceptionalMnemonics = ["ORG", "HEX", "DEC", end]

    error_counter = 0
    string = line.split()
    words_number = len(string)

    if words_number == 1:
        if string[0] != end:
            error_counter += show_error(2, line_number)
    elif words_number == 2:
        pass
    elif words_number == 3:
        pass
    elif words_number == 4:
        pass
    else:
        error_counter += show_error(1, line_number)

    return declaration, usage, error_counter


def handle_first_element(word: str, declaration: list, mnemonics: list, line_number: int) -> tuple:
    error_counter = 0
    if not test_char(word, 'comma'):
        error_counter += show_error(4, line_number)
        declaration.append(NOTHING)
    else:
        word = word[:-1]
        state, err_c = test_basic(word, mnemonics, line_number)
        error_counter += err_c
        if state:
            declaration.append(word)
        else:
            declaration.append(NOTHING)
    return declaration, error_counter


def handle_third_element(word: str, usage: list, mnemonics: list, line_number: int) -> tuple:
    error_counter = 0
    state, err_c = test_basic(word, mnemonics, line_number)
    error_counter += err_c
    if state:
        usage.append(word)
    else:
        usage.append(NOTHING)
    return usage, error_counter


def handle_fourth_element(word: str, line_number) -> int:
    error_counter = 0
    if test_char(word, 'first'):
        error_counter += show_error(3, line_number)
    else:
        if not test_char(word, 'i'):
            error_counter += show_error(5, line_number)
    return error_counter


def handle_exceptional_cases(word: str, mnemonic: str, mnemonics: list, exceptional_mnemonics: list, declaration: list,
                             usage: list,
                             line_number: int) -> tuple:
    error_counter = 0
    i = test_exceptional_mnemonics(mnemonic, exceptional_mnemonics)
    if i == 0:
        if not compare_list_string(word, mnemonics):
            error_counter += show_error(6, line_number)
        usage, err_c = handle_third_element(word, usage, mnemonics, line_number)
        error_counter += err_c
    elif i == 1:
        usage, err_c = test_hexadecimal_case(word, usage, line_number)
        error_counter += err_c
    elif i == 2:
        pass
    elif i == 3:
        pass
    return declaration, usage, error_counter


def test_basic(word: str, mnemonics: list, line_number: int) -> tuple:
    error_counter = 0
    state = True
    if test_char(word, 'first'):
        error_counter += show_error(3, line_number)
        state = False
    if not test_char(word, 'length'):
        error_counter += show_error(12, line_number)
        state = False
    if compare_list_string(word, mnemonics):
        error_counter += show_error(7, line_number)
        state = False
    return state, error_counter


def test_char(word: str, mode: str) -> bool:
    if mode == 'first':
        return word[0].isdigit()
    elif mode == 'comma':
        return word[-1] == ','
    elif mode == 'i':
        return word == 'i'
    elif mode == 'length':
        return test_word_len(word, 3)


def test_word_len(word: str, length: int) -> bool:
    return len(word) == length


def test_exceptional_mnemonics(mnemonic: str, exceptional_mnemonics: list):
    for i in range(4):
        if exceptional_mnemonics[i] == mnemonic:
            if i == 0:
                return 1
            else:
                return i
    return 0


def test_hexadecimal_case(word: str, usage: list, line_number: int) -> tuple:
    error_counter = 0
    if not test_word_len(word, 4):
        error_counter += show_error(13, line_number)
    if not test_hexadecimal(word):
        error_counter += show_error(14, line_number)
    usage.append(NOTHING)
    return usage, error_counter


def test_hexadecimal(word: str):
    for i in word:
        if not ('0' <= i <= '9') and not ('A' <= i <= 'F'):
            return False
    return True


def compare_list_string(word: str, s_list: list) -> bool:
    for i in s_list:
        if i == word:
            return True
    return False


def show_error(error_code: int, line_number: int):
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

    return 1
