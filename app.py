from flask import Flask, render_template, request

import syllable_separator_hu
from syllable_separator_hu import Hyphenation

app = Flask(__name__)
hyphenator = syllable_separator_hu.Hyphenation  # Creates an instance of the Hyphenation class

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/hyphenate', methods=['POST'])
def hyphenate():
    word = request.form.get('word')
    result = hyphenator.Hyphenation() if word else "Please enter a word."
    return render_template('index.html', result=result, word=word)

if __name__ == '__main__':
    app.run(debug=True)
