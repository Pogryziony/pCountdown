import sys


def printStartupMessage():
    try:
        time = int(input('Enter seconds: '))
    except ValueError:
        sys.exit("WRONG TYPE!")
    return time


class MessageController:
    pass
