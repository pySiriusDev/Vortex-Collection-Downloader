from os import system, name as osname


stop = False


def clearScreen() -> None:
    system('cls' if osname == 'nt' else 'clear')
