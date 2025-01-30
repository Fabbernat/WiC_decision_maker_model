import spacy
import re

class Model:

    def get_word_context(self, word, sentence):
        """Returns surrounding words of the target word in a sentence."""
        words = sentence.split()
        if word in words:
            index = words.index(word)
            left_context = words[max(0, index - 2): index]  # Get up to 2 words before
            right_context = words[index + 1: index + 3]  # Get up to 2 words after
            return set(left_context + right_context)
        return set()

    def determine_word_similarity(self, word, sentence_a, sentence_b):
        """Determines if the word has the same meaning in two different sentences based on context similarity."""
        context_a = self.get_word_context(word, sentence_a)
        context_b = self.get_word_context(word, sentence_b)

        # If there are common words in both contexts, assume the meaning is the same
        similarity = len(context_a & context_b) / (len(context_a | context_b) + 1e-5)  # Avoid division by zero

        return "YES" if similarity > 0 else "NO"

    def process_question(self, question):
        """Extracts components from the formatted question and determines the answer."""
        match = re.match(r'Does the word "(.+?)" mean the same thing in sentences "(.+?)" and "(.+?)"\?', question)
        if not match:
            return "Invalid question format"

        word, sentence_a, sentence_b = match.groups()
        return self.determine_word_similarity(word, sentence_a, sentence_b)

# Example usage:
'''
word = "run"
sentence_a = "I went for a run in the park."
sentence_b = "The play had a long run on Broadway."
context_a = {"for", "a", "in", "the"}
context_b = {"a", "long", "on", "Broadway"}
similarity = len(context_a & context_b) / (len(context_a | context_b) + 1e-5)
common_words = context_a & context_b = {"a"}
total_words = context_a | context_b = {"for", "a", "in", "the", "long", "on", "Broadway"}

similarity = len({"a"}) / len({"for", "a", "in", "the", "long", "on", "Broadway"})
           = 1 / 7
           = 0.14
return "YES" if similarity > 0 else "NO"
'''

questions = []
questions.append('Does the word "run" mean the same thing in sentences "I went for a run in the park." and "The play had a long run on Broadway."?')
questions.append('Does the word "defeat" mean the same thing in sentences "It was a narrow defeat." and "The army \'s only defeat ."?')
questions.append('Does the word "bank" mean the same thing in sentences "Bank on your good education." and "The pilot had to bank the aircraft"?')

model = Model()
for question in questions:
    print(model.process_question(question))

