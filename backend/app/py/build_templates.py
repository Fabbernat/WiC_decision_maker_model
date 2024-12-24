import csv
<<<<<<< HEAD


def read_dataset():
    # Az adatfájl betöltése
    with open('../../dataset/test/test.data.txt', 'r', encoding='utf-8') as file:
=======
import os


def read_dataset():
    # Get the directory of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the absolute path to the dataset
    dataset_path = os.path.join(current_dir, '../../dataset/test/test.data.txt')
    # Az adatfájl betöltése
    with open(dataset_path, 'r', encoding='utf-8') as file:
>>>>>>> origin/dev
        reader = csv.reader(file, delimiter='\t')  # Tabulátorral elválasztott adatok olvasása
        data = list(reader)  # A teljes adat beolvasása a fájl lezárása előtt
    return data  # Az adat visszaadása a fájl lezárása után


def chat_template(word, s1, s2):
    return (f'Does the word "{word}" mean the same in sentence "{s1}" as in sentence "'
<<<<<<< HEAD
            f'{s2}"?')


def template_builder(endindex):  # you can adjust how many lines you want to work with
=======
            f'{s2}"?\n')


def template_builder(endindex, reverse=False):  # you can adjust how many lines you want to work with
>>>>>>> origin/dev
    i = 0
    string_builder = []
    data = read_dataset()
    print(data)
    for row in data:
        target_word = row[0]
<<<<<<< HEAD
        PoS = row[1]
        index1_index2 = row[2]
        example_1 = row[3]
        example_2 = row[4]
        question = chat_template(target_word, example_1, example_2)
        string_builder.append(question)
        i += 1
        if i > endindex:
=======
        _PoS = row[1]
        index1_index2 = row[2]
        if not reverse:
            example_1 = row[3]
            example_2 = row[4]
        else:
            example_1 = row[4]
            example_2 = row[3]
        question = chat_template(target_word, example_1, example_2)
        string_builder.append(question)
        i += 1
        if i >= endindex:
>>>>>>> origin/dev
            break

    return ''.join(string_builder)