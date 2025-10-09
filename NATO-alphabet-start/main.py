import pandas

while True:

        input_Word = input("Your name: ").upper()


        data = pandas.read_csv("nato_phonetic_alphabet.csv")

        for i in input_Word:
            try:
                item = [[element["letter"], element["code"]] for _, element in data.iterrows() if element["letter"] == i]
            except:
                print("Sorry But Input sahi krr")
            else:
                print(f"{item[0][0]} for {item[0][1]}")