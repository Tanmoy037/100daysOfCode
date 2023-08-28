# import csv 

# with  open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     for row in data:
#         print(row)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(data["temp"])

data_dict = data.to_dict()
print(data_dict) 

temp_list = data["temp"].to_list()
print(len(temp_list))

print(data["temp"].max())