
import sys

MENU = {
    "espresso": {
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

COINS_TO_USD = {
    "quarter": 0.25,
    "dime": 0.10,
    "nickle": 0.05,
    "penny": 0.01
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def get_report():
    for key in resources:
        if key == 'money':
            print(f"{key}: ${resources[key]}")
        else:
            print(f"{key}: {resources[key]}")

def check_drink_resources(drink):
    selected_drink = MENU[drink]
    selected_drink_ingredients = selected_drink['ingredients']

    for ingredient in selected_drink_ingredients:
        if selected_drink_ingredients[ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
        else:
            return True

def consume_resources(drink):
    selected_drink_ingredients = MENU[drink]['ingredients']

    for ingredient in selected_drink_ingredients:
        resources[ingredient] -= selected_drink_ingredients[ingredient]


def increase_money(amount):
    if 'money' in resources:
        resources['money'] += amount
    else:
        resources['money'] = 0
        resources['money'] += amount


def check_insered_coins_with_drink_price(insered_coins,drink):
    drink_cost = MENU[drink]['cost']
    if insered_coins > drink_cost:
        change = round(insered_coins - drink_cost, 2)
        print(f"“Here is ${change} dollars in change.")
    elif insered_coins < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return
    consume_resources(drink)
    print("Here is your latte ☕️. Enjoy!")

    increase_money(drink_cost)



def insert_coins():
    drink_price = 0
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    drink_price += quarters* COINS_TO_USD['quarter']

    dimes = int(input("how many dimes?: "))
    drink_price += quarters* COINS_TO_USD['dime']

    nickles = int(input("how many nickles?: "))
    drink_price += quarters* COINS_TO_USD['nickle']

    pennies = int(input("how many pennies?: "))
    drink_price += quarters* COINS_TO_USD['penny']

    return drink_price

request = ''

while request != 'off':
    request = input("What would you like? (espresso/latte/cappuccino): ")

    if request == "report":
        get_report()
    elif request == "off":
        sys.exit()
    elif request == "espresso" or request == "latte" or request == "cappuccino":
        are_ressources_available = check_drink_resources(request)

        if are_ressources_available:
            user_money = insert_coins()
            check_insered_coins_with_drink_price(user_money,request)








