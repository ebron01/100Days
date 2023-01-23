import pandas as pd

squirrel_data = pd.read_csv("/home/beast/100Days/squirrel/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
key_list = squirrel_data["Primary Fur Color"].unique().tolist()

numbers = []
for key in key_list[1:]:
    numbers.append(len(squirrel_data[squirrel_data["Primary Fur Color"] == key]))

fur_counts = { "Fur Color" : key_list[1:], "Count" : numbers}
fur_pd = pd.DataFrame(fur_counts)
fur_pd.to_csv("/home/beast/100Days/squirrel/squirrel_count.csv")
