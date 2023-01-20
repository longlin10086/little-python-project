import os
import art

print(art.logo)


flag = True
members = {}
while flag:
    members_len = len(members)
    print("Welcome to the secret auction program.")
    print(f"Now {members_len} people are in front of you.")
    name = input("What is your name?: ")
    bid = input("What's your bid?: $")
    members[name] = bid
    should_run = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if should_run[0] == "n":
        flag = False
    os.system('cls')

val = 0
tmp = ""
for member in members:
    if int(members[member]) > val:
        val = int(members[member])
        tmp = member

print(f"The winner is {tmp} with a bid of ${val}.")

