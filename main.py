from CountdownController import countdown
from MessageController import printStartupMessage


def start():
    countdown(printStartupMessage())


class Main:
    start()
