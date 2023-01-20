from art import logo
import random
import os

cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
card_real = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
player_cards_real = []
computer_cards = []
computer_cards_real = []


def init():
    player_cards.clear()
    player_cards_real.clear()
    computer_cards.clear()
    computer_cards_real.clear()


def final_compare():
    if player_cards.count("A") == computer_cards.count("A"):
        print("You are draw.")
    elif player_cards.count("A") > computer_cards.count("A"):
        print("You win!")
    else:
        print("You lose")
    init()


def test_computer(computer):
    while computer < 17:
        print("It's time for computer to hit one card.")
        index = cards.index(random.choice(cards))
        computer_cards.append(cards[index])
        computer += card_real[index]
        print("The computer's cards are:")
        print(" ".join(computer_cards))

    if computer > 21 and "A" in computer_cards:
        computer -= 10

    return computer


def over():
    player_score = sum(player_cards_real)
    computer_score = sum(computer_cards_real)
    print("The computer's cards are:")
    print(" ".join(computer_cards))
    if test_computer(computer_score) > 21:
        print("You win!")
        init()
        return

    if player_cards.count("A") > 1 or computer_cards.count("A") > 1:
        final_compare()
        return

    if "A" in player_cards and player_score > 21:
        player_score -= 10

    if player_score > 21:
        print("You lose.")
        return
    else:
        if player_score > computer_score:
            print("You win!")
        elif player_score == computer_score:
            print("You are draw.")
        else:
            print("You lose.")
        init()


def hit():
    player = cards.index(random.choice(cards))
    player_cards.append(cards[player])
    player_cards_real.append(card_real[player])
    print("Your cards are:")
    print(" ".join(player_cards))

    player_score = sum(player_cards_real)
    if "A" in player_cards and player_score > 21:
        player_score -= 10
    if player_score > 21:
        print("You lose.")
        init()
        return

    choice_hit = input("Do you want to 'hit', 'stand', or 'surrender'?\n").lower()
    if choice_hit == "hit":
        hit()
    elif choice_hit == "stand":
        over()
    else:
        print("You lose!")
        init()


if __name__ == '__main__':
    want_to_play = input("Do you want to play BlackJack with the computer? Type 'yes' or 'no'.\n").lower()
    if want_to_play[0] == "n":
        exit(0)

    should_continue = True
    while should_continue:
        print(logo)

        for _ in range(2):
            player_index = cards.index(random.choice(cards))
            computer_index = cards.index(random.choice(cards))
            player_cards.append(cards[player_index])
            player_cards_real.append(card_real[player_index])
            computer_cards.append(cards[computer_index])
            computer_cards_real.append(card_real[computer_index])

        print(f"The computer's cards are: {computer_cards[0]} _")
        print("Your cards are:")
        print(" ".join(player_cards))

        choice = input("Do you want to 'hit', 'stand', or 'surrender'?\n").lower()
        if choice == "hit":
            hit()
        elif choice == "stand":
            over()
        else:
            print("You lose!")
            init()

        want_to_continue = input("Do you want to try again? Type 'yes' or 'no'.\n").lower()
        if want_to_continue[0] == "n":
            should_continue = False
        else:
            os.system("cls")
