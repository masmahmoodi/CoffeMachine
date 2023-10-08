things = {
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
quarters = 0.25
dimes = 0.10
nickles = 0.05
pennies = 0.01
money = 0


def checking_money(price, calculate_change, kindOf_coffe):
    if calculate_change >= price:
        calculate_change -= price
        global money
        money += price
        print(f"here is your change {round(calculate_change, 2)}")
        print(f"enjoy your {kindOf_coffe}")
    else:
        print("sorry enter much money , money refunded")


def enough_resources(ingridients):
    for key in ingridients:
        resources[key] -= ingridients[key]


def insert_coins():
    print("please insert the coins . ")
    input_quarters = float(input("how many quarters ? "))
    input_dimes = float(input("how many dimes ? "))
    input_nickles = float(input("how many nickles ? "))
    input_pennies = float(input("how many pennies ? "))
    #      total_enter = input_quarters + input_dimes + input_nickles +input_pennies
    return input_quarters * quarters + input_dimes * dimes + input_nickles * nickles + input_pennies * pennies


def checking_resource(ingridients):
    for key in ingridients:
        if resources[key] < ingridients[key]:
            print(f"sorry we don't have much {key}")
            return False
    return True


off = False
while not off:
    kindOf_coffe = input("What would you like ? (espresso/lattt/cappuccino): ").lower()
    if kindOf_coffe == "espresso" or kindOf_coffe == "cappuccino" or kindOf_coffe == "latte":
        dirnk = things[kindOf_coffe]
        if checking_resource(dirnk['ingredients']):
            calculate_change = insert_coins()
            enough_resources(dirnk['ingredients'])
            checking_money(dirnk['cost'], calculate_change, kindOf_coffe)
        else:
            off = True
            break
    elif kindOf_coffe == "report":
        print(
            f"water:{resources['water']}ml\nmilk:{resources['milk']}ml\ncoffe:{resources['coffee']}ml\nmoney:${money}")
    elif kindOf_coffe == "off":
        off = True

    else:
        print("not exist!!")
