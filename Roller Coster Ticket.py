print("Welcome to this Roller Coster Ride")
Bill=0
height = int(input("What's your height? \n"))

if height >= 120:
    age = int(input("Good! You can ride but What's your age? \n"))
    if age <= 12:
        print("Your ticket is $5")
        Bill += 5
    elif 12 > age <=18:
        print("Your ticket is $7")
        Bill += 7
    elif age > 18:
        print("Your ticket is $12")
        Bill += 12

    Photo = input("Do you want photos as well? It would cost $3 extra. Y/N\n")

    if Photo == "Y":
        Bill += 3

    elif Photo == "N":
        Bill += 0

    print(f"Ok \nYour total bill is ${Bill}\nEnjoy the Ride.")

else:
    print("You can't ride! You better grow up.")