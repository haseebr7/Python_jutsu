import random

number = random.randint(1,101)

print("""

  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ' _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|        
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.

""")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
number_of_guesses = 0
if difficulty == "easy":
    number_of_guesses += 10
elif difficulty == "hard":
    number_of_guesses += 5
print(f"You have {number_of_guesses} number of guesses")
Game_over = True
while Game_over:
    while number_of_guesses != 0:

        guess = int(input("Guess the number:  "))

        if guess > number:
            print("Your guess is too high.")
        elif guess < number:
            print("Your guess is too low.")
        else:
            print(f"You guessed it Correctly! That number was {number}")
            break
        number_of_guesses -= 1
        if number_of_guesses == 0:
            print(f"You are out of fuel!!!\n You losed!!! The correct number was {number}")
            break
        else:
            print(f"{number_of_guesses} Guesses are left")
    play_again = input("Do you wanna play again! Y/N ").lower()
    if play_again == "n":
        Game_over = False