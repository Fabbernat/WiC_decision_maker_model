import curses
from argparse import ArgumentError


# open console app:
def my_curses_init(*args):
    needed_arguments = 2
    stdscr = curses.initscr()
    stdscr.clear()
    try:
        stdscr.addstr(10, 10, args[0])
        stdscr.addstr(15, 25, args[1])
    except:
        raise ArgumentError(None, f"Message: wrong parameterization. You should pass {needed_arguments} arguments to this function"
        )
    stdscr.refresh()
    stdscr.getch()