num = 5
list1 = []
final_num = 1
for i in range(1,num+1):
    list1.append(i)
for i in list1:
    final_num *= i

print(final_num)