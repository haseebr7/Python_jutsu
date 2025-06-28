MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 150,
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

def resources_checkup(coffee_type):
    global ask_for_money
    if MENU[coffee_type]["ingredients"]["water"] <= resources["water"]:
        if MENU[coffee_type]["ingredients"]["milk"] <= resources["milk"]:
            if MENU[coffee_type]["ingredients"]["coffee"] <= resources["coffee"]:
                print("ingredients are sufficent")
                ask_for_money = True
            else:
                print("ingredients are insufficent")
                ask_for_money = False
        else:
            print("ingredients are insufficent")
            ask_for_money = False
    else:
        print("ingredients are insufficent")
        ask_for_money = False

def coins_cal(coin25, coin10, coin5, coin1):
    Total_coins = 0
    Total_coins += (coin25 * 0.25)
    Total_coins += (coin10 * 0.10)
    Total_coins += (coin5 * 0.05)
    Total_coins += (coin1 * 0.01)
    print(f"coffee price: {MENU[select_coffee]["cost"]} Amount paid: {Total_coins}")
    return  Total_coins


while True:
    select_coffee = input("What would you like? (espresso/latte/cappuccino): ")

    ask_for_money = False

    if select_coffee == "report":
        print(resources)

    elif select_coffee == "espresso" or "latte" or "cappuccino":
        resources_checkup(select_coffee)


    while ask_for_money:
        Quarter = int(input("Enter Quarter coins $0.25: "))
        Dime  = int(input("Enter Dime coins $0.10: "))
        Nickel  = int(input("Enter Nickel  coins $0.05: "))
        Penny = int(input("Enter Penny coins $0.01: "))


        if coins_cal(Quarter, Dime, Nickel, Penny) > MENU[select_coffee]["cost"]:
            resources["water"] -= MENU[select_coffee]["ingredients"]["water"]
            resources["milk"] -= MENU[select_coffee]["ingredients"]["milk"]
            resources["coffee"] -= MENU[select_coffee]["ingredients"]["coffee"]
            print(f"Here is your ☕ coffee and change ${coins_cal(Quarter, Dime, Nickel, Penny) - MENU[select_coffee]["cost"]}")
        else:
            print("Coins are not sufficient")
        ask_for_money = False
