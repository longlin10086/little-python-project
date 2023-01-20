from data import MENU, resources

resources_remain = resources
resources_remain["money"] = 0


def calculate():
    print("Please insert coins.")
    quarter = int(input("How many quarters?: "))
    dime = int(input("How many dimes?: "))
    nickle = int(input("How many nickles?: "))
    penny = int(input("How many pennies?: "))
    return 0.01*penny+0.05*nickle+0.1*dime+0.25*quarter


def print_report():
    print(f"Water: {resources_remain['water']}ml")
    print(f"Milk: {resources_remain['milk']}ml")
    print(f"Coffee: {resources_remain['coffee']}g")
    print(f"Money: ${resources_remain['money']}")


def detective(answer):
    if answer[0] == "r":
        print_report()
        return False

    if answer == "off":
        exit(0)

    if answer[0] not in ["e", "l", "c"]:
        print("Sorry, I don't have this kind of coffee.")
        return False

    for item in MENU[answer]["ingredients"]:
        if resources_remain[item] < MENU[answer]["ingredients"][item]:
            print(f"Sorry there is not enough {item}.")
            return False

    user_money = calculate()
    if user_money < MENU[answer]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False

    for item in MENU[answer]["ingredients"]:
        resources_remain[item] -= MENU[answer]["ingredients"][item]

    resources_remain["money"] += MENU[answer]["cost"]
    print(f"Here are the changes: ${round(user_money-MENU[answer]['cost'], 2)}")
    print(f"Here is your {answer}. Enjoyed.")
    return True


if __name__ == '__main__':
    while True:
        user_answer = input("What would you like?(espresso/latte/cappuccino):").lower()
        detective(user_answer)
        print("Thank you for using the machine.")
