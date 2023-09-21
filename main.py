menu = {
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
	"money": 2.5,
}

#TODO make different functions for each type of coffee

power = True

def check_money(type):
	global menu
	global resources
	print(f"Required amount of money is {menu[type]['cost']}")
	q = int(input("Number of quarters: "))
	d = int(input("Number of dimes: "))
	n = int(input("Number of nickles: "))
	p = int(input("Number of pennies: "))

	mon = 0.25*q + 0.1*d + 0.05*n + 0.01*p
	print(f"You have given {mon}")
	if mon < menu[type]["cost"]:
		print("Insufficient amount of money, order rejected, money refunded")
	else:
		resources["money"] = resources["money"] + menu[type]["cost"]
		print(f"Here is your change of amount {mon - menu[type]['cost']} ")
		making(type1)


def making(type):
	global resources
	global menu
	for stuff in menu[type]["ingredients"]:
		resources[stuff] = resources[stuff] - menu[type]["ingredients"][stuff]
	print(f"Here is your {type}")







def coffee_machine(type):
	global resources
	global menu
	global power

	not_enough = False

	if type == "report":
		print(resources)
	elif type == "power off":
		print("Shutting down!")
		power = False
	else:
		for stuff in menu[type]["ingredients"]:
			if resources[stuff] < menu[type]["ingredients"][stuff]:
				print(f"Sorry, not enough {stuff}!")
				not_enough = True
				break
		if not_enough == False:
			check_money(type1)




while power:
	type1 = input("What would you like? espresso/latte/cappuccino ").lower()
	coffee_machine(type1)



