from flask import Flask, render_template
import nlp_utils
app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)
    # Example usage
    sample_text = "Hello, World! This is a test.    Normalize  this text, please!"
    tokens = nlp_utils.normalize_and_tokenize(sample_text)
    print(tokens)
