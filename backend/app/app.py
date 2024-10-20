import os
import curses

from flask import Flask, render_template
from curses import wrapper
from py import build_templates, curses_init

# import nlp_utils

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':

    # Az adatfájl betöltése
    templates = build_templates.template_builder(10)

    # Ensure output directory exists
    output_dir = 'output'
    os.makedirs(output_dir, exist_ok=True)

    # Open the file in write mode
    with open('output/out.txt', 'w', encoding='utf-8') as f:
        print('Answer with a single "YES" or "NO"!', file=f)
        print(templates, file=f, end="")
    f.close()  # force close the file to speed up the app

    reversed_templates = build_templates.template_builder(10, reverse=True)
    # Open the file in write mode
    with open('output/out_reversed.txt', 'w', encoding='utf-8') as reversed_f:
        print('Answer with a single "YES" or "NO"!', file=reversed_f)
        print(reversed_templates, file=reversed_f, end="")
    reversed_f.close()



    wrapper(curses_init)

    app.run(host="127.0.0.1", port=5000, debug=True)


def py():
    return None
