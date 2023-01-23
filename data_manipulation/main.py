# with open("/home/beast/100Days/data_manipulation/weather_data.csv") as f:
#     data = f.readlines()
# for index in range(len(data)):
#     data[index] = data[index].strip() 
# print(data)

# import csv 

# temperatures = []
# with open("/home/beast/100Days/data_manipulation/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     for row in data:
#         if row[1] == "temp":
#             continue
#         temperatures.append(int(row[1]))
# print(temperatures)

import pandas as pd

data = pd.read_csv("/home/beast/100Days/data_manipulation/weather_data.csv")

data_dict = data.to_dict()
print(data_dict)
print(data.keys())
print(data.temp)
print(data["temp"].mean())
print(data["temp"].max())

#get data in the row
print(data[data.temp == data.temp.max()])

#create a dataframe from scratch
data_dict = {
    "students" : ["Amy" , "James", "Angela"],
    "scores" : [76, 59, 65]
    }
new_data = pd.DataFrame(data_dict)
new_data.to_csv("/home/beast/100Days/data_manipulation/new_data.csv")