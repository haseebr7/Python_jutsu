#Final Working Code

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "("]
import random

print("Welcome to Pygenerator")
Letter_input = int(input("How many letters you want?\n"))
Number_input = int(input("How many Number you want?\n"))
Symbol_input = int(input("How many Symbol you want?\n"))
password = []

for L in range(1, Letter_input+1):
    Choice = random.choice(letters)
    password += Choice

for N in range(1, Number_input+1):
    Choice = random.choice(numbers)
    password += Choice

for S in range(1, Symbol_input+1):
    Choice = random.choice(symbols)
    password += Choice

random.shuffle(password)
Final=""
for i in password:
    Final += i
print(Final)

# Well, I think, I nailed it.