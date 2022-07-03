import math
import sys
import time


def countdown(timeInSeconds):
    try:
        minutes = math.floor(timeInSeconds / 60)
        secondsLeft = timeInSeconds % 60
        while timeInSeconds >= 0:
            print('Time left: ', minutes, ':', secondsLeft)
            if secondsLeft == 0 and minutes > 0:
                minutes -= 1
                secondsLeft = 60
            elif secondsLeft == 0 and minutes == 0:
                break
            time.sleep(1)
            secondsLeft -= 1
    except KeyboardInterrupt:
        sys.exit('Countdown interrupted')


class CountdownController:
    pass
