#num = 0
# for i in range(1, 101):
#     num += i
# print(num)

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        i = "fizzbizz"
    elif i % 5 == 0:
        i="bizz"
    elif i % 3 == 0:
        i = "fizz"


    print(i)