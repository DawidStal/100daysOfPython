import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_phonetic_alphabet = pandas.read_csv("Day 26 Nato Alphabet\\nato_phonetic_alphabet.csv")
nato_alphabet = {row.letter: row.code for (index, row) in nato_phonetic_alphabet.iterrows()}


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_answer():
    word = [letter for letter in input("Enter a word: ").upper()]
    try:
        nato_words = [nato_alphabet[letter] for letter in word]
    except KeyError as error:
        print(f"There is no letter {error} in the alphabet")
        generate_answer()
    else:
        print(nato_words)


generate_answer()
