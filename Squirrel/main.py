import pandas

data = pandas.read_csv("squirrel-data.csv")
squirrel_color_data = data["Highlights in Fur Color"]
white = 0
Gray = 0
Cinnamon = 0


Gray_color_data = len(data[data["Primary Fur Color"] == "Gray"])
Black_color_data = len(data[data["Primary Fur Color"] == "Black"])
Cinnamon_color_data = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(Gray_color_data)



# for i in squirrel_color_data:
#     if i == "White":
#         white += 1
#     elif i == "Gray":
#         Gray += 1
#     elif i == "Cinnamon":
#         Cinnamon += 1

colored_squirrels = {
    "colors" : ["Black", "Gray", "Cinnamon"],
    "quantity" : [Black_color_data,Gray_color_data,Cinnamon_color_data]
}
sq_data = pandas.DataFrame(colored_squirrels)
sq_data.to_csv("colored_squirrels`")
