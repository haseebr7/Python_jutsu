import random
from game_data import data
from art import logo
from art import vs
print(logo)
def num():
    return random.randint(1, 50)

first_entry = data[num()]
second_entry = data[num()]

Game_over = True
score = 0
while Game_over:

    print(f"First entry is {first_entry["name"],first_entry["follower_count"],first_entry["description"],first_entry["country"]}")
    print(vs)
    print(f"Second entry is {second_entry["name"],second_entry["follower_count"],second_entry["description"],second_entry["country"]}")
    print(f"Your score {score}")
    guess = input("Which number is greater A/B: ").lower()

    if guess == "a":
        if first_entry["follower_count"] >= second_entry["follower_count"]:
            print("You are right!!!")
            first_entry = second_entry
            score += 1
        elif second_entry["follower_count"] >= first_entry["follower_count"]:
            print("You are wrong")
            Game_over = False

    elif guess == "b":
        if first_entry["follower_count"] <= second_entry["follower_count"]:
            print("You are right!!!")
            first_entry = second_entry
            score += 1
        elif second_entry["follower_count"] <= first_entry["follower_count"]:
            print("You are wrong")
            Game_over = False
    second_entry = data[num()]

