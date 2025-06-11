#Faulty one
import random
Random_Num = random.randint(1, 3)
Input_from_user = int(input("Enter Rock 1,Paper 2 or Scissor 3"))

if Random_Num == 1 and Input_from_user == 2:

    print(f"Com Move: {Random_Num} \nUser Win")
elif Random_Num == 2 and Input_from_user == 3:
    print(f"Com Move: {Random_Num} \nUser Win")
elif Random_Num == 3 and Input_from_user == 1:
    print(f"Com Move: {Random_Num} \nUser Win")
elif Random_Num == 1 and Input_from_user == 1:
    print(f"Com Move: {Random_Num} \nDraw")
elif Random_Num == 2 and Input_from_user == 2:
    print(f"Com Move: {Random_Num} \nDraw")
elif Random_Num == 3 and Input_from_user == 3:
    print(f"Com Move: {Random_Num} \nDraw")
else:
    print(f"Com Move: {Random_Num}\nCom Win")