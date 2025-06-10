weight = 85
height = 1.85

bmi = weight / (height ** 2)


print(bmi)
if bmi <= 18.5:
    print("Under weight")
elif 18.5 < bmi < 24.9:
    print("Normal")
elif 25 < bmi < 29.9:
    print("Over weight")
else:
    print("Evacuate this person, NOW!!!")