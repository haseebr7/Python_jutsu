def calculate_love_score(name1, name2):
    cal = 0
    cal2 = 0
    for i in name1 + name2:
        for u in "true":
            if i == u:
                cal += 1
        for u in "love":
            if i == u:
                cal2 += 1

    print(str(cal) + str(cal2))


calculate_love_score("kanye west","kim kardashian")