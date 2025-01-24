# PATH: C:\PycharmProjects\WiC_decision_maker_model\app\consoleapp.py
# Console app

from app.py.controllers.MenuController import MenuController

import sys
import threading

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
    main()