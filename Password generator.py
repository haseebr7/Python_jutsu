# Again Faulty code


letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "("]
import random


print("Welcome to Pygenerator")
Letter_input = 3#int(input("How many letters you want?\n"))
Number_input = 3#int(input("How many Number you want?\n"))
Symbol_input = 1#int(input("How many Symbol you want?\n"))
password = ""

Randomizer = [1,2,3]


Calculate_password_digits = (Letter_input + Number_input + Symbol_input)
print(Calculate_password_digits)

for i in range(1,Calculate_password_digits+1):
    Randomizer_choice = random.choice(Randomizer)
    if Randomizer_choice == 1:
        Choice = random.choice(letters)
        password += str(Choice)
    elif Randomizer_choice == 2:
        Choice = random.choice(numbers)
        password += str(Choice)

    elif Randomizer_choice == 3:
        Choice = random.choice(symbols)
        password += str(Choice)


print(password)