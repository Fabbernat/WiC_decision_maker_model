import os
import sys
import threading
from random import choice

from backend.app.py import build_templates
from backend.app.py.controllers.MenuController import MenuController


def run_flask():
    app.run(host="127.0.0.1", port=5000, debug=True)

from flask import Flask, render_template


# import nlp_utils

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


def my_curses_app(file_content):

    stdscr = initscr()
    curs_set(0)  # Rejtse el a kurzort
    stdscr.clear()
    my_curses_init.my_curses_init(templates, reversed_templates)
    # Fájl tartalmának megjelenítése a konzolon
    for idx, line in enumerate(file_content):
        stdscr.addstr(idx, 0, line.strip())

    # Felhasználói input figyelése
    while True:
        stdscr.addstr(len(file_content) + 1, 0, "Type 'stop' to exit: ")
        stdscr.refresh()

        # Felhasználói input beolvasása
        user_input = stdscr.getstr(len(file_content) + 2, 0, 20).decode("utf-8")

        # Kilépés a "stop" beírására
        if user_input.lower() == 'stop':
            break

    stdscr.clear()
    stdscr.addstr(0, 0, "Exiting...")
    stdscr.refresh()
    napms(1000)

def main():
    print("Welcome to my app!")
    mc = MenuController()
    mc.display_menu()

    choice = sys.stdin.readline()

    # Az adatfájl betöltése
    templates = build_templates.template_builder(10)

    # Ensure output directory exists
    output_dir = 'output'
    os.makedirs(output_dir, exist_ok=True)

    # Open the file in write mode
    with open(f'{output_dir}/out.txt', 'w', encoding='utf-8') as f:
        print('Answer with a single "YES" or "NO"!', file=f)
        print(templates, file=f, end="")
    f.close()  # force close the file to speed up the app

    reversed_templates = build_templates.template_builder(10, reverse=True)
    # Open the file in write mode
    with open(f'{output_dir}/out_reversed.txt', 'w', encoding='utf-8') as reversed_f:
        print('Answer with a single "YES" or "NO"!', file=reversed_f)
        print(reversed_templates, file=reversed_f, end="")
    reversed_f.close()

    # screen handling
    if len(sys.argv) > 0:
        file_path = sys.argv[0]
    run_flask()

if __name__ == '__main__':
    # Start Flask server in a separate thread
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()

    # Continue with curses UI or other tasks here
    main()

def py():
    return None
