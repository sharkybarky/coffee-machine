MENU = {
    "expresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": [300, 'ml'],
    "milk": [200, 'ml'],
    "coffee": [100, 'g']
}


def check_resources(coffee, res):
    coffee_ingredients = MENU[coffee]["ingredients"]
    for key in coffee_ingredients.keys():
        if res[key][0] < coffee_ingredients[key]:
            print(f"Not enough {key} for {coffee}")
            return False
    return True


def process_coins(choice):
    cost = MENU[choice]["cost"]
    print(f"Chose expresso, that costs ${cost:0.2f}.")
    num_quarters = int(input("How many $0.25 coins inserted? "))
    total = num_quarters * 0.25
    print(f"Balance ${total:0.2f}")
    num_dimes = int(input("How many $0.10 coins inserted? "))
    total += num_dimes * 0.10
    print(f"Balance ${total:0.2f}")
    num_nickels = int(input("How many $0.05 coins inserted? "))
    total += num_nickels * 0.05
    print(f"Balance ${total:0.2f}")
    num_pennies = int(input("How many $0.01 coins inserted? "))
    total += num_pennies * 0.01
    print(f"Balance ${total:0.2f}")

    if total >= cost:
        if total > cost:
            print(f"Paid too much, change of ${total - cost:0.2f} returned")
        return cost
    else:
        print("Sorry that's not enough money. Money refunded.")
        return 0


def print_report(money):
    for key, value in resources.items():
        print(f"{key.title()}: {value[0]}{value[1]}")
    print(f"Money: ${money:0.2f}")


def make_coffee(choice, res):
    print(f"Making a {choice}. Here you go!")
    choice_ingredients = dict(MENU[choice]["ingredients"])
    for ingredient in choice_ingredients:
        res[ingredient][0] -= choice_ingredients[ingredient]
    # res.update({key: [res[key][0] - choice_ingredients.get(key), res[key][1]] for key in choice_ingredients})


def process_input(sales):
    choice_char = input("What would you like? 'e'xpresso, 'l'atte, 'c'appuccino: ")
    takings = 0
    match choice_char:
        case "e" | "expresso":
            choice = "expresso"
        case "l" | "latte":
            choice = "latte"
        case "c" | "cappuccino":
            choice = "cappuccino"
        case "off":
            print("SECRET WORD: Machine turning off...")
            return False, 0
        case "report":
            print_report(sales)
            return True, 0
        case _:
            print("Invalid option!")
            return True, 0

    if check_resources(choice, resources):
        takings = process_coins(choice)
        if takings > 0:
            make_coffee(choice, resources)
    else:
        print(f"Not enough resources for that choice! Sorry please try another choice")

    return True, takings


def run():
    in_operation = True
    sales = 0.0
    while in_operation:
        in_operation, takings = process_input(sales)
        sales += takings


run()

