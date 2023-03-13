"""Simple blind typing trainer console app.

Multiplatform functionality in progress.

To quit the app, simply type ESC."""

import os
import sys
from random import randint
from time import time
from getch import Getch



def gen_word(size = None):
    """Generates random string containing lowercase
      characters of English alphabet"""
    if size is None:
        size = randint(3, 10)
    char = ''
    for i in range(size):
        char += chr(randint(ord('a'), ord('z')))
    return char


def gen_sentence(sent_len):
    """Generates random sentence, containing random
      generated words."""
    if sent_len is None:
        sent_len = randint(3, 10)
    sent = ''
    for i in range(sent_len):
        sent += gen_word() + ' '
    return sent[:-1]


def clear_screen():
    """Clears terminal screen"""
    if sys.argv[1] == '-u':
        clear = 'clear'
    else:
        clear = 'cls'
    os.system(clear)


def trainer(st):
    """Main trainer fucntion for Windows OS.
    Clears the terminal, shows app a sequence that must
    be typed in, replaces the letters that typed correctly with '*'"""
    errors_count = 0
    for i, elem in enumerate(st):
        while True:
            clear_screen()
            print(st)
            getch = Getch()

            inp = getch()
            if inp == bytes(elem, encoding='utf-8'):
                st = list(st)
                st[i] = '*'
                st = ''.join(st)
                break
            else:
                errors_count += 1

            if inp == b'\x1b':
                clear_screen()
                sys.exit()

    clear_screen()
    print('*'*len(st))
    return len(st), errors_count


def run_trainer(sent_size = None, errors_cost = 0, flag = True):
    """Main function"""
    start = time()
    size, errors = trainer(gen_sentence(sent_size))
    spent_time = time() - start
    print('='*size, f'\nCharacters count = {size}. Done {errors} mistakes. Spent {spent_time} seconds.')
    print(f'Speed = {size/spent_time} char/sec')
    errors_added = spent_time + errors*errors_cost
    print(f'Errors cost added: Time = {errors_added}, speed = {size/errors_added}')
    ans = input('Do you want to save your result? (y/n)')
    if ans == 'y':
        if flag:
            save_result(errors_added, size, errors)
        else:
            print("You can't save resaults, because you changed default error cost settings")


def save_result(spent_time, size, errors):      # TODO add hash generation, for checking veracity.
    name = input('Input your name: ')
    with open('results.txt', 'a') as f:
        f.write(f'Name: {name}, Line len: {size}, Mistakes: {errors}, Spent time: {spent_time}, Speed: {size/spent_time}\n')
        f.close()


def load_results():         #TODO add leaderboard
    with open('results.txt', 'r') as f:
        lines = f.readlines()
        print('Last results: \n')
        for i in lines:
            print(i)


def menu():
    getch = Getch()
    default_size = None
    default_error_cost = 5
    can_save_flag = True
    while True:
        print('Welcome to kb trainer, implemented by Garik Mk')
        print('1. Start new session')
        print('2. View current records')
        print('3. Settings')
        print('4. Quit')
        try:
            inp = str(getch(), encoding='utf-8')
        except UnicodeDecodeError:
            inp = '0'
        match inp:
            case '1':
                run_trainer(default_size, default_error_cost, can_save_flag)
                clear_screen()
            case '2':
                load_results()
                getch()
            case '3':
                clear_screen()
                print('===== Settings =====')
                print('1. Change sent len')
                print('2. Change error cost')
                print('3. Set default values')
                inp2 = str(getch(), encoding='utf-8')
                match inp2:
                    case '1':
                        default_size = int(input())
                    case '2':
                        default_error_cost = abs(int(input()))
                        if default_error_cost != 5:
                            can_save_flag = False
                    case '3':
                        default_size = None
                        default_error_cost = 5
                clear_screen()
            case '4':
                sys.exit()
        clear_screen()


if __name__ == '__main__':
    menu()
