# print("Welcome to a top Calculator!")
#
# Bill = float(input("What's the total bill? \n"))
# Tip = int(input("How much the tip would you like to give?(In percentage) \n"))
# peoples = int(input("How many peoples are going to split the bill? \n"))
#
# Calculated_Tip =  (Tip/100) * Bill
#
# Splited_bill = (Bill + Calculated_Tip) / peoples
# print(f"Well total tip is ${Calculated_Tip} and Total bill is around ${(Bill + Calculated_Tip)}")
# print(f"Sooo, each one of you have to pay ${round(Splited_bill,2)} if you don't wanna wash the dishes....So Choice is yours...")

import random
from random import shuffle

list="dsfdsafsdafdsf"

random.shuffle(list)
print(list)