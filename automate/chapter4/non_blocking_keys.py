import sys
import select
import tty
import termios
import time


def isData():
    return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])


old_settings = termios.tcgetattr(sys.stdin)
try:
    tty.setcbreak(sys.stdin.fileno())

    i = 0
    while 1:
        print(i)
        time.sleep(1)  # Add a 1-second pause to reduce flickering.
        i += 1

        if isData():
            c = sys.stdin.read(1)
            if c == "\x1b":  # x1b is ESC
                break

finally:
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
