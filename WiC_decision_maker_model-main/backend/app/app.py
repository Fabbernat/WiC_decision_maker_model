import data
import pandas as pd
from flask import Flask, render_template
from py import build_templates

# import nlp_utils

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':

    # Az adatfájl betöltése
    templates = build_templates.template_builder(10)
    # Open the file in write mode
    with open('output/out.txt', 'w', encoding='utf-8') as f:
        for element in templates:
            print(element, file=f, end="")

    app.run(host="127.0.0.1", port=5000, debug=True)


def py():
    return None
