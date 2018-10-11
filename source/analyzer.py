from source.__config__ import ALONE_IN_LINE
from source.__config__ import MRI
from source.__config__ import NON_MRI
from source.__config__ import PREUDOMSTRUCTION


def analyzer(line: str, declaration: set, usage: set, line_number: int) -> tuple:
    error_counter = 0
    strings = line.split()
    words_number = len(strings)

    if words_number == 1:
        if strings[0] not in ALONE_IN_LINE:
            error_counter += show_error(2, line_number)

    elif words_number == 2:
        declaration, usage, err_c = handle_exceptional_cases(strings[1], strings[0], declaration, usage, line_number)
        error_counter += err_c

    elif words_number == 3:
        if strings[0] in MRI and strings[1] not in MRI:
            a = 1
        elif strings[1] in MRI and strings[0] not in MRI:
            a = 2
        else:
            a = 0
            error_counter += show_error(8, line_number)
        if a != 0:
            declaration, usage, err_c = handle_exceptional_cases(strings[a], strings[a - 1], declaration, usage,
                                                                 line_number)
            error_counter += err_c
            if a == 1:
                error_counter += handle_fourth_element(strings[2], line_number)
            elif a == 2:
                declaration, err_c = handle_first_element(strings[0], declaration, line_number)
                error_counter += err_c

    elif words_number == 4:
        declaration, usage, err_c = handle_exceptional_cases(strings[2], strings[1], declaration, usage, line_number)
        error_counter += err_c
        if strings[1] not in ALONE_IN_LINE:
            declaration, err_c = handle_first_element(strings[0], declaration, line_number)
            error_counter += err_c
            error_counter += handle_fourth_element(strings[3], line_number)
    else:
        error_counter += show_error(1, line_number)

    return declaration, usage, error_counter


def handle_first_element(word: str, declaration: set, line_number: int) -> tuple:
    error_counter = 0
    if not test_char(word, 'comma'):
        error_counter += show_error(4, line_number)
    else:
        word = word[:-1]
        state, err_c = test_basic(word, [MRI, NON_MRI, PREUDOMSTRUCTION], line_number)
        error_counter += err_c
        if state:
            declaration.add(word)
    return declaration, error_counter


def handle_third_element(word: str, usage: set, line_number: int) -> tuple:
    error_counter = 0
    state, err_c = test_basic(word, [MRI, NON_MRI, PREUDOMSTRUCTION], line_number)
    error_counter += err_c
    if state:
        usage.add(word)
    return usage, error_counter


def handle_fourth_element(word: str, line_number: int) -> int:
    error_counter = 0
    if not test_char(word, 'i'):
        error_counter += show_error(5, line_number)
    return error_counter


def handle_exceptional_cases(word: str, mnemonic: str, declaration: set, usage: set, line_number: int) -> tuple:
    error_counter = 0
    i = test_exceptional_mnemonics(mnemonic)
    if i == -1:
        if not compare_database_string(mnemonic, MRI):
            error_counter += show_error(6, line_number)
        else:
            usage, err_c = handle_third_element(word, usage, line_number)
            error_counter += err_c
    elif i == 0 or i == 1:
        error_counter += test_hexadecimal_case(word, line_number)
    elif i == 2:
        error_counter += test_decimal_case(word, line_number)
    elif i == 3:
        error_counter += show_error(16, line_number)
    return declaration, usage, error_counter


def test_basic(word: str, database, line_number: int) -> tuple:
    error_counter = 0
    state = True
    if test_char(word, 'first'):
        error_counter += show_error(3, line_number)
        state = False
    if not test_char(word, 'length'):
        error_counter += show_error(11, line_number)
        state = False
    if compare_database_string(word, database):
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


def test_exceptional_mnemonics(mnemonic: str):
    if mnemonic in PREUDOMSTRUCTION[1:3]:
        return PREUDOMSTRUCTION.index(mnemonic)
    elif mnemonic in ALONE_IN_LINE:
        return 3
    else:
        return -1


def test_hexadecimal_case(word: str, line_number: int) -> int:
    error_counter = 0
    if not test_word_len(word, 4):
        error_counter += show_error(12, line_number)
    else:
        if not test_hexadecimal(word):
            error_counter += show_error(13, line_number)
    return error_counter


def test_hexadecimal(word: str) -> bool:
    for i in word:
        if not ('0' <= i <= '9') and not ('A' <= i <= 'F'):
            return False
    return True


def test_decimal_case(word: str, line_number: int) -> int:
    error_counter = 0
    if word[0] == '-':
        word = word[1:]
    if word.isdecimal():
        num = int(word)
        if num < -32768 or 32767 < num:
            error_counter += show_error(14, line_number)
    else:
        error_counter += show_error(15, line_number)
    return error_counter


def compare_database_string(word: str, database) -> bool:
    return word in database


def show_error(error_code: int, line_number: int):
    error_text_list = ["Unexpected Error\n",
                       "Exceeded max words [4] in one line limit.\n",
                       "Only MRI symbols and END symbol can be alone in one line of code.\n",
                       "First character of variable/function/command can't be digits.\n",
                       "First element in this line of code should be finished with ','.\n",
                       "Last element in \"this\" line of code should be \"i\".\n",
                       "Can't recognize mnemonic\n",
                       "Using system reserved mnemonics for variable/function is forbidden. \n",
                       "Invalid syntax.",
                       "The variable/function is not defined. \n",
                       "First element of line can't be only ','. \n",
                       "Variable/function name can't be more than 3 characters.\n",
                       "Hexadecimal number must be in range 0000 to FFFF.\n",
                       "Hexadecimal number should come after ORG/HEX mnemonic.\n",
                       "Decimal number must be signed 2 byte integer (in range -32768 to 32767).\n",
                       "Decimal number should come after DEC mnemonic.\n",
                       "Using non-MRI mnemonics or END with other elements isn't correct .\n",
                       "Invalid error code."]
    print("(line => {}) ERROR: ".format(line_number) + error_text_list[error_code])
    return 1
