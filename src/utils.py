import os


CLEAR_ANSI = 0 # print \033[2J
CLEAR_CLS = 1 # windows cls command
CLEAR_CLEAR = 2 # unix clear command


def clear(method: int = None):
    if method == CLEAR_ANSI:
        print('\033[2J')
    elif method == CLEAR_CLS:
        os.system('cls')
    elif method == CLEAR_CLEAR:
        os.system('clear')
    else:
        print('\033[2J')
