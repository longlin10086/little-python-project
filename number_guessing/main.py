from art import logo
import random
import os


user_guessed_number = []


def difficulty():
    attempts_initial = 10
    difficult_level = input("Choose a difficulty. Type 'easy' of 'hard': ").lower()
    if difficult_level[0] == "h":
        attempts_initial = 6
    elif difficult_level[0] == "q":
        exit(0)
    return attempts_initial


def guess():
    goal = random.randint(1, 100)
    attempts = difficulty()

    while attempts != 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        print("You can type 'quit' at any time to quit.")
        user_type = input("Make a guess: ").lower()
        if user_type[0] == "q":
            exit(0)
        else:
            user_number = int(user_type)

        if user_number in user_guessed_number:
            print("You have already guessed the number.Try again.")
            attempts += 1
        elif user_number == goal:
            print("You get it!")
            break
        elif user_number > goal:
            print("Too high.")
        else:
            print("Too low.")
        print("Guess again.")
        user_guessed_number.append(user_number)
        attempts -= 1

    if attempts == 0:
        print("You lose.")
    print(f"The answer is {goal}.")


if __name__ == '__main__':
    while True:
        print(logo)
        print("Welcome to the Number Guessing Game!")
        print("I'm thinking of a number between 1 and 100.")
        guess()

        if input("Do you want to play again? Type 'yes' or 'no'.").lower()[0] == "n":
            os.system("cls")
            break
        else:
            user_guessed_number.clear()
            os.system("cls")
