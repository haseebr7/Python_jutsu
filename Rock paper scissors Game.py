Rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

Paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

Scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
import random
List = [0,1,2]
Com_move = random.choice(List)
User_move = int(input("Choice Rock(0),Paper(1),Scissors(2)"))

# User's move Visual
print("User Move")
if User_move == 0:
    print(Rock)
elif User_move == 1:
    print(Paper)
elif User_move == 2:
    print(Scissors)

# Com's move Visual

print("Com Move")

if Com_move == 0:
    print(Rock)
elif Com_move == 1:
    print(Paper)
elif Com_move == 2:
    print(Scissors)



if User_move == 0 and Com_move == 1:
    print("Com Win")
elif User_move == 1 and Com_move == 2:
    print("Com Win")
elif User_move == 2 and Com_move ==0:
    print("Com Win")
elif User_move == Com_move:
    print("Draw")
elif User_move != 0 and User_move != 1 and User_move != 2:
    print("You typed Invalid number...")
else:
    print("User Win")


