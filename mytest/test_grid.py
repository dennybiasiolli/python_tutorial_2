#!/usr/bin/env python
import sys
import termios
import contextlib

from grid import Grid


@contextlib.contextmanager
def raw_mode(file):
    old_attrs = termios.tcgetattr(file.fileno())
    new_attrs = old_attrs[:]
    new_attrs[3] = new_attrs[3] & ~(termios.ECHO | termios.ICANON)
    try:
        termios.tcsetattr(file.fileno(), termios.TCSADRAIN, new_attrs)
        yield
    finally:
        termios.tcsetattr(file.fileno(), termios.TCSADRAIN, old_attrs)

def dead(why):
    print why
    # exit(0)

def main():
    grid = Grid()
    grid.print_position('')
    # while True:
    #     input_chars = raw_input('Insert direction [w, a, s, d], \'q\' to quit: ')
    #     input_chars = input_chars.lower()
    #     for char in input_chars:
    #         if char == 'x' or char == 'q':
    #             dead('Bye bye!')
    #         elif char not in ['w', 'a', 's', 'd']:
    #             print 'Wrong direction!'
    #         else:
    #             if(grid.move(char)):
    #                 dead('Treasure found, great!')
    print 'exit with ^C or ^D'
    with raw_mode(sys.stdin):
        try:
            while True:
                char = sys.stdin.read(1)
                char = char.lower()
                if not char or char == chr(4):
                    break
                if char == 'x' or char == 'q':
                    dead('Bye bye!')
                    break
                elif char not in ['w', 'a', 's', 'd']:
                    print 'Wrong direction!'
                else:
                    if(grid.move(char)):
                        dead('Treasure found, great!')
                        break
        except (KeyboardInterrupt, EOFError):
            pass


if __name__ == '__main__':
    main()
