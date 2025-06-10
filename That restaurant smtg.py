print("Welcome to Pizza Heart Liver")
Bill=0

Size = input("Which size pizza do you want? S, M or L: \n")
Pepperoni = input("Do you want pepperoni? Y/N: \n")
Cheese = input("Do you want extra cheese? Y/N: \n")

if Size == "S":
    Bill += 15
elif Size == "M":
    Bill += 20
elif Size == "L":
    Bill += 25

if Pepperoni == "Y":
    if Size == "S":
        Bill += 2
    else:
        Bill += 3
if Cheese == "Y":
    Bill += 3

print(f"You final bill in {Bill}")