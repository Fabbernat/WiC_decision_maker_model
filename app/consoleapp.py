# PATH: C:\PycharmProjects\WiC_decision_maker_model\app\consoleapp.py
# Console app

from app.py.controllers.MenuController import MenuController
from app.py import TemplateBuilder

import sys
import threading
import os
import app.py.WordSenseDisambiguator


def tryparse(input_str, type_func=int):
    try:
        return type_func(input_str.strip())  # Strip to remove trailing newline/spaces
    except ValueError:
        return None

def main():
    print("Welcome to my app!")
    while True:
        mc = MenuController()
        mc.display_menu()

        input_str = sys.stdin.readline()
        choice = tryparse(input_str, int)

        if choice is None:
            print("Invalid input. Please enter a valid number.")
        else:
            print(f"You selected option {choice}.")
        if choice == 0:
            exit(0)
        if choice == 1:
            print('Enter the question!')
            question = sys.stdin.readline()
            Model.wsd(question)
            # Az adatfájl betöltése
            tb = TemplateBuilder.TemplateBuilder()
            templates = tb.build_templates(10)

            # Ensure output directory exists
            output_dir = 'output'
            os.makedirs(output_dir, exist_ok=True)

            # Open the file in write mode
            print('Answer with a single "YES" or "NO"!')
            print(templates, end="")

            reversed_templates = tb.build_templates(10, reverse=True)
            # Open the file in write mode
            print('Answer with a single "YES" or "NO"!')
            print(reversed_templates, end="")


if __name__ == '__main__':
    main()