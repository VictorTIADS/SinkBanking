def printBold(text, enter=False):
    print(f"\033[1m{text}\033[0m")
    if enter:
        print()


def printRed(text, enter=False):
    print(f"\033[91m{text}\033[0m")
    if enter:
        print()


def printBlue(text, enter=False):
    print(f"\033[96m{text}\033[0m")
    if enter:
        print()


def printGreen(text, enter=False):
    print(f"\033[92m{text}\033[0m")
    if enter:
        print()


def printPurple(text, enter=False):
    print(f"\033[95m{text}\033[0m")
    if enter:
        print()


def printWhite(text, enter=False):
    print(f"\033[34m{text}\033[0m")
    if enter:
        print()


def printYellow(text, enter=False):
    print(f"\033[33m{text}\033[0m")
    if enter:
        print()
