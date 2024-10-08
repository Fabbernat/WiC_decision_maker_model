from transformers import AutoModelForSequenceClassification, AutoTokenizer

model_name = "google/gemma-2-2b-it"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

def classify_pair(sentence1, sentence2, word):
    inputs = tokenizer.encode_plus(sentence1, sentence2, return_tensors='pt', truncation=True)
    outputs = model(**inputs)
    logits = outputs.logits
    prediction = logits.argmax(dim=-1).item()
    return prediction

# Teszteljük a példapárokat
for index, row in data.iterrows():
    sentence1 = row['sentence1']
    sentence2 = row['sentence2']
    word = row['word']
    result = classify_pair(sentence1, sentence2, word)
    print(f"Sentence pair {index}: {result}")
