import csv


def read_dataset():
    # Az adatfájl betöltése
    with open('../dataset/test/test.data.txt', 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter='\t')  # Tabulátorral elválasztott adatok olvasása
        data = list(reader)  # A teljes adat beolvasása a fájl lezárása előtt
    return data  # Az adat visszaadása a fájl lezárása után


def chat_template(word, s1, s2):
    return (f'Does the word {word} mean the same in sentence "{s1}" as in sentence"'
            f'{s2}"?')


if __name__ == '__main__':
    AI = None
    data = read_dataset()
    for row in data:
        target_word = row[0]
        PoS = row[1]
        index1_index2 = row[2]
        example_1 = row[3]
        example_2 = row[4]
        question = chat_template(target_word, example_1, example_2)
        print(question)
    # TODO AI.ask(question)
