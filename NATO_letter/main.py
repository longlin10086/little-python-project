import pandas

dataframe = pandas.read_csv("nato_phonetic_alphabet.csv")

dictionary = {row.letter: row.code for (index, row) in dataframe.iterrows()}

user_name = input("Please input the word you want to convert: ").upper()
for letter in user_name:
    print(dictionary[letter])
# for (index, row) in student_data_frame.iterrows():

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

