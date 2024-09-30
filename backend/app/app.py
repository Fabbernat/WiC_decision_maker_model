import data
import pandas as pd
from flask import Flask, render_template
from py import build_templates
# import nlp_utils

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')





def count_word_occurrences(sentences, word):
    count = 0
    for sentence in sentences:
        count += sentence.split().count(word)
    return count


if __name__ == '__main__':

    # Az adatfájl betöltése
    templates = build_templates.template_builder
    for element in templates:
        print(element)
    # print(chat_template("bed", "There's a lot of trash on the bed of the river",
    #                     "I keep a glass of water next to my bed when I sleep"))
    app.run(host="127.0.0.1", port=5000, debug=True)


def py():
    return None
