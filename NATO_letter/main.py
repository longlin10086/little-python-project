import pandas

dataframe = pandas.read_csv("nato_phonetic_alphabet.csv")

dictionary = {row.letter: row.code for (index, row) in dataframe.iterrows()}
is_on = True
word_list = []
while is_on:
    user_name = input("Please input the word you want to convert: ").upper()
    is_on = False
    for letter in user_name:
        try:
            word_list.append(dictionary[letter])
        except KeyError:
            print("Please input a word whose letters are all in alphabet")
            is_on = True
            break

print(word_list)
# for (index, row) in student_data_frame.iterrows():

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

