from random import randint
import os


class _Getch:
    """Gets a single character from standard input.  Does not echo to the
screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()

class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()


def gen_string(size = 10):
    st = ''
    for i in range(size):
        st += chr(randint(ord('a'), ord('z')))
    return st


def trainer(st):
    for i, s in enumerate(st):
        while True:
            os.system('clear')
            print(st)
            os.system("stty -echo")
            getch = _Getch()

            if getch() == s:
                os.system("stty echo")
                st = list(st)
                st[i] = '*'
                st = ''.join(st)
                os.system('clear')
                break

if __name__ == '__main__':
    trainer(gen_string())




