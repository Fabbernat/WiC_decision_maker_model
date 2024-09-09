import data
import pandas as pd
from flask import Flask, render_template

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
    data = pd.read_csv('../dataset/test/test.data.txt', delimiter='\t')
    for element in data:
        print(element)
    # print(chat_template("bed", "There's a lot of trash on the bed of the river",
    #                     "I keep a glass of water next to my bed when I sleep"))
    app.run(host="127.0.0.1", port=5000, debug=True)
