# with open("weather_data.csv") as weather_info:
#     weather_data = weather_info.readlines()
# print(weather_data)

# import CSV
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     # for row in data:
#     #     print(row)
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].tolist()
# print(temp_list)

# temperatura medie dintr-o lista
# sum = 0
# for temp in temp_list:
#     sum = sum + temp
# average_temp = sum/len(temp_list)
# print(average_temp)

# average_temp = sum(temp_list) / len(temp_list)
# print(average_temp)

# print(data["temp"].mean())

# maximum_temp = max(temp_list)
# print(maximum_temp)

# print(data["temp"].max())

# print(data.condition)

# print(data[data.day == "Monday"])

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_F = (monday_temp * 9)/5 + 32
# print(monday_temp_F)

# create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

import csv
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
print(black_squirrel_count)
print(gray_squirrel_count)
print(cinnamon_squirrel_count)

data_dict = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Count": [gray_squirrel_count, black_squirrel_count, cinnamon_squirrel_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")