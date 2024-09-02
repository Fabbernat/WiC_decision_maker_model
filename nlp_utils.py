# nlp_utils.py
from nltk.tokenize import word_tokenize

import re
import string
import nltk
nltk.download('punkt')


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

# Ensure the necessary NLTK data is downloaded
nltk.download('punkt')


def tokenize_text(text):
    # Tokenize the text into words
    t_tokens = word_tokenize(text)
    return t_tokens


# Example usage
tokens = tokenize_text(normalized_text)
print(tokens)


# Combined normalization and tokenization script

def normalize_and_tokenize(text):
    nat_normalized_text = normalize_text(text)
    nat_tokens = tokenize_text(nat_normalized_text)
    return nat_tokens
