from flask import Flask, render_template
from syllable_separator_hu import Hyphenation

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/')
def main():
    hyphenator = Hyphenation  # Create an instance of the Hyphenation class
    result = str(hyphenator)    # Call the __str__ method to get the string output
    return f"<pre>{result}</pre>"  # Return the result wrapped in <pre> tags for formatting

if __name__ == '__main__':
    app.run()
