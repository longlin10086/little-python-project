import random
import hangman_words
import hangman_art
import os

print(hangman_art.logo)
print("Pssst,the solution is thriftless.")
word = []
guessed_word = []
lives = 6
chosen_word = random.choice(hangman_words.word_list)
word_len = len(chosen_word)
# print(f"the chosen word is {chosen_word}")

for _ in range(word_len):
    word.append("_")
print(" ".join(word))
print("Try to guess it and save the life.")

end_of_game = False

while not end_of_game:
    char_user = input("guess a character:\n").lower()
    os.system("cls")
    for char_index in range(word_len):
        char = chosen_word[char_index]
        if char_user == char:
            word[char_index] = char
            print("Ok, you guessed it.")
    if char_user in guessed_word:
        print("You have already guessed the character.Try again.")

    if char_user not in chosen_word and char_user not in guessed_word:
        lives -= 1
        print(f"You guessed {char_user}, that's not in the word. You lose a life.")
        print(hangman_art.stages[lives])
    print(" ".join(word))
    guessed_word += char_user
    if "_" not in word:
        end_of_game = True
        print("You win!")

    if lives == 0:
        end_of_game = True
        print("You lose!")
        print(f"The answer is {chosen_word}.")
