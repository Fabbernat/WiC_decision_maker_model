# nlp_utils.py
# from nltk.tokenize import word_tokenize

import re
import string
# import nltk

# Ensure the necessary NLTK data is downloaded
# nltk.download('punkt')


def normalize_text(text):
    # Convert text to lowercase
    text = text.lower()

    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()

    return text


# Example usage
sample_text = "Hello, World! This is a test.    Normalize  this text, please!"
normalized_text = normalize_text(sample_text)
print(normalized_text)


'''
def tokenize_text(text):
    # Tokenize the text into words
    tokens = word_tokenize(text)
    print("Tokenization succesful!")
    return tokens
'''


# Example usage
tokens = tokenize_text(normalized_text)
print(tokens)


# Combined normalization and tokenization script

def normalize_and_tokenize(text):
    normalized_text = normalize_text(text)
    tokens = tokenize_text(normalized_text)
    return tokens


def read_input_data():
    return open("../../dataset/dev/dev.data.txt", "r")
