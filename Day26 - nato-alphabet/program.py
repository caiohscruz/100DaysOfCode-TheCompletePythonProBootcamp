import pandas as pd

nato_dataframe = pd.read_csv("nato_phonetic_alphabet.csv")

# print(nato_alphabet)

# TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}

nato_dictionary = {row.letter: row.code for (index, row) in nato_dataframe.iterrows()}

# print(nato_dictionary)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# TODO 3. Add Exception Treatment


def get_nato_transcription():
    user_input = input("Type a word: ").upper()
    try:
        transcription = [nato_dictionary[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        get_nato_transcription()
    else:
        print(transcription)


get_nato_transcription()