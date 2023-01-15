from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine


def run():
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    in_operation = True
    while in_operation:
        choice_char = input(f"What would you like from the menu? {menu.get_items()}: ")
        match choice_char:
            case "e" | "expresso":
                drink = menu.find_drink("espresso")
            case "l" | "latte":
                drink = menu.find_drink("latte")
            case "c" | "cappuccino":
                drink = menu.find_drink("cappuccino")
            case "off":
                print("SECRET WORD: Machine turning off...")
                in_operation = False
                continue
            case "report":
                print("SECRET WORD: Report of machine:")
                coffee_maker.report()
                money_machine.report()
                continue
            case _:
                print("Invalid option!")
                continue

        print(f"You have chosen {drink.name} which costs ${drink.cost:0.2f}.")
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)


run()
