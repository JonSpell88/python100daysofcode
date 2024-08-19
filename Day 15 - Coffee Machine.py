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
    "revenue": 0
}

def print_report():
    print(f"We have {resources["water"]} ml of Water.")
    print(f"We have {resources["milk"]} ml of Milk.")
    print(f"We have {resources["coffee"]} g of Coffee.")
    print(f"We have ${resources["revenue"]} of Revenue.")

# check against current resources to see if we can make the drink
def can_we_make_the_drink(drink_choice):
    if drink_choice == "espresso":
        if resources["water"] >= MENU["espresso"]["ingredients"]["water"] and \
            resources["coffee"] >= MENU["espresso"]["ingredients"]["coffee"]:
            return True
        else:
            return False
    elif drink_choice == "latte":
        if resources["water"] >= MENU["latte"]["ingredients"]["water"] and \
            resources["coffee"] >= MENU["latte"]["ingredients"]["coffee"] and \
            resources["milk"] >= MENU["latte"]["ingredients"]["milk"]:
            return True
        else:
            return False
    elif drink_choice == "cappuccino":
        if resources["water"] >= MENU["cappuccino"]["ingredients"]["water"] and \
            resources["coffee"] >= MENU["cappuccino"]["ingredients"]["coffee"] and \
            resources["milk"] >= MENU["cappuccino"]["ingredients"]["milk"]:
            return True
        else:
            return False
    else:
        print("Sorry, that was an invalid choice.")
        return False


# process coins, add up values, check against drink price, return change, add revenue to resources
def process_payment(q, d, n, p, drink_choice):
    total_payment = (q * 0.25) + (d * 0.10) + (n * 0.05) + (p * .01)
    if total_payment == MENU[drink_choice]["cost"]:
        print("Thank you for using exact change!")
        resources["revenue"] += MENU[drink_choice]["cost"]
        return True # successful payment
    elif total_payment < MENU[drink_choice]["cost"]:
        print(f"Insufficient funds. The cost of the {drink_choice} is {MENU[drink_choice]["cost"]}")
        print(f"and you only gave us ${total_payment}")
        print("We will refund your money.")
        return False # unsuccessful payment
    elif total_payment > MENU[drink_choice]["cost"]:
        overpayment = total_payment - MENU[drink_choice]["cost"]
        print(f"You overpaid by {overpayment}. We will refund that amount back to you.")
        resources["revenue"] += MENU[drink_choice]["cost"]
        return True

# make drink, deduce resources, run can we make it first
def make_the_drink(drink_choice):
    if drink_choice == "espresso":
        resources["water"] -= MENU[drink_choice]["ingredients"]["water"]
        resources["coffee"] -= MENU[drink_choice]["ingredients"]["coffee"]
    elif drink_choice in ("latte", 'cappuccino'):
        resources["water"] -= MENU[drink_choice]["ingredients"]["water"]
        resources["coffee"] -= MENU[drink_choice]["ingredients"]["coffee"]
        resources["milk"] -= MENU[drink_choice]["ingredients"]["milk"]
    else:
        print("That was not a valid choice.")

# start of processing
print("Welcome to the Coffee Machine!")
choice = input("What kind of drink would you like? espresso, latte or cappuccino? ")
while choice != "exit":     # hidden choice
    if choice.lower() == "report":  # hidden choice
        print_report()
    elif can_we_make_the_drink(choice.lower()) == True:
        print(f"The price of {choice} is ${MENU[choice]["cost"]}")
        quarters = float(input("How many quarters inserted? "))
        dimes = float(input("How many dimes inserted? "))
        nickels = float(input("How many nickels inserted? "))
        pennies = float(input("How many pennies inserted? "))   # do coin-ops even take pennies?

        if process_payment(quarters, dimes, nickels, pennies, choice) == True:
            make_the_drink(choice)
            print(f"Enjoy your {choice}!")
    elif can_we_make_the_drink(choice.lower()) == False:
        print(f"We have insufficient ingredients to make a {choice}")
    else:   # to catch anything else
        print("That was an invalid choice. Please try again.")

    choice = input("What kind of drink would you like? espresso, latte or cappuccino? ")
# exit while loop
print("Thanks for stopping by!")



