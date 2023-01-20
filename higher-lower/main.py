import art
from data import data
import random
import os

used_data = []
score = 0
history_score = 0


def init():
    global score
    used_data.clear()
    score = 0
    os.system("cls")


def vs(data_first, data_second):
    print(f"Compare A: {data_first['name']}, a {data_first['description']}, from {data_first['country']}")
    print(art.vs)
    print(f"Against B: {data_second['name']}, a {data_second['description']}, from {data_second['country']}")
    return input("Who has more followers? Type 'A' or 'B'.").lower()


def compare(data_first, data_second):
    return data_first['follower_count'] > data_second['follower_count']


def game(data_first):
    global score
    global history_score
    print(art.logo)
    print(f"The highest score in history is {history_score}.")
    print(f"Your current score is {score}.")
    data_b = random.choice(data)
    while data_b in used_data:
        data_b = random.choice(data)
    used_data.append(data_b)
    answer = vs(data_first, data_b)
    if answer == 'a' and compare(data_first, data_b):
        score += 1
        os.system("cls")
        game(data_first)
    elif answer == 'b' and compare(data_b, data_first):
        score += 1
        os.system("cls")
        game(data_b)
    else:
        print("You lose!")
        print(f"You final score is {score}.")
        if score > history_score:
            history_score = score


if __name__ == '__main__':
    if input("Do you want to play The Higher-Lower Game? Type 'yes' or 'no'.\n").lower()[0] == "n":
        exit(0)

    while True:
        A = random.choice(data)
        used_data.append(A)
        game(A)

        if input("Do you want to play again? Type 'yes' or 'no'.").lower()[0] == "n":
            break
        else:
            init()

