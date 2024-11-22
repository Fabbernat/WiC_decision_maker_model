# Provided dataset
import feladat


words = [
    "egylet", "egység", "egymás", "egyszeregy", "egyablakos", "egyágú", "egyágyas",
    "egyárbocos", "egyemeletes", "egyértelmű", "egyéves", "egyezer", "egyfelvonásos",
    "egyfülű", "egyhangú", "egyidejű", "egyirányú", "egyjegyű", "egykarú", "egykedvű",
    "egykezű", "egylábú", "egylaki", "egymillió", "egynapos", "egyoldalú", "egyöntetű",
    "egypetéjű", "egypólusú", "egypúpú", "egyrészes", "egysejtű", "egysínű", "egysoros",
    "egyszarvú", "egyszáz", "egyszemű", "egyszikű", "egyszínű", "egyszobás", "egyszólamú",
    "együgyű", "együléses", "egyvágányú", "mintegy", "egynéhány", "egyes", "első",
    "elseje", "először", "egyszer", "egyszeres", "egyesével", "egyenként", "egyedül",
    "egyed", "együtt", "egyéb", "egyes", "egyedül", "egyenlő", "egyenes", "egyértelmű",
    "egyszerű", "együtt", "egyébként", "egyesült", "egyetem", "egymás", "egykori",
    "egyaránt", "egység", "egyéni", "együttműködés", "egyszerre"
]

# Define rules for suffix validity based on Hungarian usage
# "egy" should be treated as a suffix in words where it forms meaningful compound words
valid_suffix_examples = {"egység", "egyke", "egyszer", "együgyű"}
invalid_suffix_examples = {"egyetem", "egyezkedik", "együttműködés", "egyenként", "egyenes", "egyedül"}

# Count occurrences of correct and incorrect cases
correct_count = 0
incorrect_count = 0
classified_words = {"correct": [], "incorrect": []}

for word in words:
    # Check if "egy" as a suffix would create a meaningful split based on example categories
    if any(word.endswith(example) for example in valid_suffix_examples):
        correct_count += 1
        classified_words["correct"].append(word)
    elif any(word.startswith(example) or word.endswith(example) for example in invalid_suffix_examples):
        incorrect_count += 1
        classified_words["incorrect"].append(word)

# Display results
print("Correct 'egy' suffix usage count:", correct_count)
print("Incorrect 'egy' suffix usage count:", incorrect_count)
print("\nWords classified as correct:")
print(", ".join(classified_words["correct"]))
print("\nWords classified as incorrect:")
print(", ".join(classified_words["incorrect"]))

for word in words:
    print(feladat.elvalasztas(word))
