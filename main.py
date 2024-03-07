drinks_list = {"coffee": 2.5, "cappuccino": 5, "mocha": 4.2, "latte": 3, "espresso": 4.3, "water": 1}


print("====================\nwelcome to coffee machine\n====================")

drinks_name = list(drinks_list.keys())
drink = input(f"please enter your drink {drinks_name}: ").lower()

if drink not in drinks_list:
    print(f"iam sorry we dont have {drink}")
    print("have a nice day")
else:
    money = float(input(f"please enter the money {drinks_list[drink]}$: "))

    if money < drinks_list[drink]:
        print(f"iam sorry the money is not enough, we cannot make your drink, here is your money ({money})")
    elif money == drinks_list[drink]:
        print(f"done, here is your {drink},enjoy:)")
    else:
        change = money - drinks_list[drink]
        print(f"done, take your change {change}, and here is your {drink},enjoy:)")

print("have a nice day")
# this is my Coffee Machine Project

