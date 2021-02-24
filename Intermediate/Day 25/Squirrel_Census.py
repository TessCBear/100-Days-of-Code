import pandas

data = pandas.read_csv(".\Intermediate\Day 25\squirrel_data.csv")

grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

squirrel_dict = {
    "Fur Colour" : ["Grey", "Cinnamon", "Black"],
    "Number of Squirrels" : [grey_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

final_data = pandas.DataFrame(squirrel_dict)
final_data.to_csv(".\Intermediate\Day 25\squirrel_data_final.csv")