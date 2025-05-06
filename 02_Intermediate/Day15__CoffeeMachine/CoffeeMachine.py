import CoffeeRessources

def report():
    resources = {
        "Water": "water",
        "Milk": "milk",
        "Coffee": "coffee",
        "Money": money
    }

    for resource, value in resources.items():
        if resource == "Money":
            print(f"{resource}: ${value}")
        elif resource == "Coffee":
            print(f"{resource}: {CoffeeRessources.resources[value]}g")
        else:
            print(f"{resource}: {CoffeeRessources.resources[value]}ml")


def coins(cost_drink):
    global money, counterfeit
    print("Please insert coins.")
    
    coin_values = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickels": 0.05,
        "pennies": 0.01
    }
    
    total = 0
    try:
        for coin, value in coin_values.items():
            coins_inserted = int(input(f"How many {coin}?: "))
            total += coins_inserted * value

        if total < cost_drink:
            print("Sorry, that's not enough. Money refunded.")
            print(f"You are missing: ${(cost_drink - total):.2f}")
            return False
        elif total > cost_drink:
            print(f"Don't forget your money: ${(total - cost_drink):.2f}")

        money += cost_drink
        return True
        
    except ValueError:
        print("Counterfeit money is prohibited in our establishment.")
        counterfeit = True
        return False


def make_it(hot_drink):
    if hot_drink not in CoffeeRessources.MENU:
        print("Invalid entry")
        return

    drink_info = CoffeeRessources.MENU[hot_drink]
    ingredients = drink_info["ingredients"]
    cost = drink_info["cost"]

    for ingredient, amount in ingredients.items():
        if CoffeeRessources.resources[ingredient] < amount:
            print(f"Sorry, there is not enough {ingredient}.")
            return

    if coins(cost):
        for ingredient, amount in ingredients.items():
            CoffeeRessources.resources[ingredient] -= amount
        print(f"Here is your {hot_drink} ☕ Enjoy!")
    else:
        if not counterfeit:
            print("Sorry, insufficient funds.")

off = False
money = 0
counterfeit = False

while not off:
    order = input("What would you like? (espresso/latte/cappuccino): ")
    if order == 'report':
        report()
    elif order == 'off':
        off = True
        print("GoodBye")
    else:
        make_it(order)