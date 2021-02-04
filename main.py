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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}




# TODO:2.  Turn off the Coffee Machine by entering “off” to the prompt.
water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
money = 0

continue_to_play = True
while continue_to_play:
    # TODO:1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    choice = input("What would you like? (espresso/latte/cappuccino):").lower()

    # TODO: 4.  Check resources sufficient?
    if choice == "latte" or choice == "cappuccino":
        water -= MENU[choice]["ingredients"]["water"]
        milk -= MENU[choice]["ingredients"]["milk"]
        coffee -= MENU[choice]["ingredients"]["coffee"]

        if water >= 0 and milk >= 0 and coffee >= 0:
            continue_to_play = True
            # TODO: 5.  Process coins.
            print("Please insert coins.")
            quarters = float(input("how many quarters?:")) * 0.25
            dimes = float(input("how many dimes?:")) * 0.10
            nickles = float(input("how many nickles?:")) * 0.05
            pennies = float(input("how many pennies?:")) * 0.01
            total_pay = quarters + dimes + nickles + pennies

            # TODO: 6.  Check transaction successful?
            change = round(total_pay - MENU[choice]["cost"], 2)
            if change < 0:
                print("Sorry that's not enough money. Money refunded.")
            elif change == 0:
                money += MENU[choice]["cost"]
                print(f"Here is your {choice} ☕️. Enjoy!")
            else:
                money += MENU[choice]["cost"]
                print(f"Here is ${change} in change.")
                print(f"Here is your {choice} ☕️. Enjoy!")
        elif water < 0:
            print("Sorry there is not enough water.")
            continue_to_play = False
        elif milk < 0:
            print("Sorry there is not enough milk.")
            continue_to_play = False
        else:
            print("Sorry there is not enough coffee.")
            continue_to_play = False

    elif choice == "espresso":
        water -= MENU[choice]["ingredients"]["water"]
        coffee -= MENU[choice]["ingredients"]["coffee"]

        if water >= 0 and coffee >= 0:
            continue_to_play = True
            # TODO: 5.  Process coins.
            print("Please insert coins.")
            quarters = float(input("how many quarters?:")) * 0.25
            dimes = float(input("how many dimes?:")) * 0.10
            nickles = float(input("how many nickles?:")) * 0.05
            pennies = float(input("how many pennies?:")) * 0.01
            total_pay = quarters + dimes + nickles + pennies

            # TODO: 6.  Check transaction successful?
            change = round(total_pay - MENU[choice]["cost"], 2)
            if change < 0:
                print("Sorry that's not enough money. Money refunded.")
            elif change == 0:
                money += MENU[choice]["cost"]
                print(f"Here is your {choice} ☕️. Enjoy!")
            else:
                money += MENU[choice]["cost"]
                print(f"Here is ${change} in change.")
                print(f"Here is your {choice} ☕️. Enjoy!")
        elif water < 0:
            print("Sorry there is not enough water.")
            continue_to_play = False
        else:
            print("Sorry there is not enough coffee.")
            continue_to_play = False

    elif choice == "off":
        continue_to_play = False
    elif choice == "report":
        print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}")
