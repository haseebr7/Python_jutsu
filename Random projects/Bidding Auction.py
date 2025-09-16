# Don't know how she did that. Mine was lil shorter

from art import logo
print(logo)
user = {
    "username": "",
    "value": 0
}
highest_number = [0]

def fun(in_name, in_big_value, highest_num):
    if in_big_value >= highest_num[0]:
        user["username"] = in_name
        user["value"] = in_big_value
        highest_num[0] = (user["value"])

Loop = True
while Loop:
    name = input("What's your name:  ")
    value = int(input("What's your bidding price:  "))
    fun(name, value, highest_number)

    other_bidders = input("Is there any other bidder: (Y)(N)")
    if other_bidders == "N":
        Loop = False
    print("\n" * 100)

print(f"{user['username']} won the bidding. His bid was {user['value']}")