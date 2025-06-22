import random
List = [11,2,3,4,5,6,7,8,9,10,10,10]

def card():
    return random.choice(List)

def total(cards_cal):
    num = 0
    for i in cards_cal:
        num += i
        if i == 11:
            if num > 21:
                num -= 10
    return num

turn_down = True

while turn_down:
    com = [card()]
    user = [card(), card()]

    turn_down = True
    while 2+2:
        com = com
        user = user

        print("Com: ",com, "=", total(com))
        print("User: ",user, "=",total(user))

        if total(user) > 21:
            print("COM win - User got numbers Above 21")
            break
        elif total(com) > 21:
            print("")
            print("USER win - Com got numbers Above 21")
            break
        if 10 in com:
            print(f"COM Win - Com got a Blackjack")
            break
        elif 10 in user:
            print(f"USER Win - User got a Blackjack")
            break

        another_round = input("To pick another Card 'Y' - To stand 'N': ").lower()
        print("-----------------------------------------")
        if "y" == another_round:
            user.append(card())

        elif "n" == another_round:
            while total(com) <= 16:
                com.append(card())
            if  total(com) > total(user) and total(com) <= 21:
                print(f"{com} = {total(com)} Com's Moves\n {user} = {total(user)} User's Moves\n--COM WINS--")

            elif total(user) > total(com):
                print(f"{com} = {total(com)} Com's Moves\n {user} = {total(user)} User's Moves\n--USER WINS--")

            else:
                print(f"{com} = {total(com)} Com's Moves\n {user} = {total(user)} User's Moves\n--It's a DRAW--")
            break

    Another_round= input("\nWant to play another round Y/N: ").lower()
    if Another_round == "n":
        turn_down = False
    else:
        print("\n"*100)