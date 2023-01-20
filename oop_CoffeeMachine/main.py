from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


if __name__ == '__main__':
    my_menu = Menu()
    my_coffee_maker = CoffeeMaker()
    my_money_machine = MoneyMachine()
    while True:
        user_answer = input(f"What would you like?({my_menu.get_items()}): ").lower()

        if user_answer[0] == "r":
            my_coffee_maker.report()
            my_money_machine.report()
            continue

        if user_answer == "off":
            exit(0)
        else:
            my_menuitem = my_menu.find_drink(user_answer)
            if my_coffee_maker.is_resource_sufficient(my_menuitem):
                # total = my_money_machine.process_coins()
                if my_money_machine.make_payment(my_menuitem.cost):
                    my_coffee_maker.make_coffee(my_menuitem)
