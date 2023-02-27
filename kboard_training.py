"""Simple blind typing trainer console app.

Multiplatform functionality in progress.

To quit the app, simply type ESC."""

import os
from random import randint
from getch import Getch



def gen_string(size = 30):
    """Generates random string containing lowercase
      characters of English alphabet"""
    st = ''
    for i in range(size):
        st += chr(randint(ord('a'), ord('z')))
    return st


def trainer_unix(st):
    """Main trainer fucntion for Unix OS.
    Clears the terminal, shows app a sequence that must
    be typed in, replaces the letters that typed correctly with '*'
    """
    for i, elem in enumerate(st):
        while True:
            os.system('clear')
            print(st)
            os.system("stty -echo")
            getch = Getch()

            inp = getch()

            if inp == elem:
                os.system("stty echo")
                st = list(st)
                st[i] = '*'
                st = ''.join(st)
                os.system('clear')
                break

            # if inp == 'q':        # TODO
            #     os.system('clear')
            #     quit()


def trainer_win(st):
    """Main trainer fucntion for Windows OS.
    Clears the terminal, shows app a sequence that must
    be typed in, replaces the letters that typed correctly with '*'"""
    for i, elem in enumerate(st):
        while True:
            os.system('cls')
            print(st)
            getch = Getch()
            
            inp = getch()
            if inp == bytes(elem, encoding='utf-8'):
                st = list(st)
                st[i] = '*'
                st = ''.join(st)
                break

            if inp == b'\x1b':
                os.system('cls')
                quit()



def main():
    # trainer(gen_string())
    trainer_win(gen_string())



if __name__ == '__main__':
    main()