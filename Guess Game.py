import random
Words = [
    "titan", "shinobi", "sharingan", "konoha", "aot", "chidori", "mangekyo", "donghua", "timetravel", "linkclick",
    "ackerman", "naruto", "kurama", "shippuden", "paradis", "reiner", "sasuke", "erwin", "minato", "xiang"
]


word = random.choice(Words)

print(word)
Guessed_letter = input("Guess a letter: ").lower()
for i in word:
    if i == Guessed_letter:
        print("Right")
    else:
        print("Wrong")