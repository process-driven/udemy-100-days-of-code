MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
global Money
Money = 0
is_on = True


def processing(drink, paid):
    global Money
    if drink in ["latte", "espresso", "cappuccino"]:
        for check in ["water", "milk", "coffee"]:
            if MENU[drink]["ingredients"][check] > resources[check]:
                print(f"Sorry! Not enough {check}")
                return
        if paid < MENU[drink]["cost"]:
            print("Sorry that's not enough money! Money refunded")
        elif paid > MENU[drink]["cost"]:
            resources["water"] -= MENU[drink]["ingredients"]["water"]
            resources["milk"] -= MENU[drink]["ingredients"]["milk"]
            resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
            Money += MENU[drink]["cost"]
            remain = round(-(MENU[drink]["cost"] - paid), 2)
            print("Here is your", drink, "Enjoy!!")
            print("You get back", remain, "dollars")
        else:
            Money += paid
            print("Here is your", drink, "Enjoy!!")
    elif drink == "report":
        print("Water:", resources["water"])
        print("Milk:", resources["milk"])
        print("Coffee:", resources["coffee"])
        print("Money:", Money)


while is_on:
    drink = input("What Do You Like To Have? (espresso,latte,cappuccino)")
    if drink == "off":
        is_on = False
    elif drink == "report":
        processing(drink, 0)
    else:
        quarters = int(input("quarters??"))
        dimes = int(input("dimes??"))
        nickles = int(input("nickles??"))
        pennies = int(input("pennies??"))
        paid = quarters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01
        processing(drink, paid)

