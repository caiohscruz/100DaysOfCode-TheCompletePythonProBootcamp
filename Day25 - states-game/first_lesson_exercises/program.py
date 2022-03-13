# import csv
#
# with open("./weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     for row in data:
#         print(row)
#

import pandas as pd

data = pd.read_csv("weather_data.csv")
print(data)

temp_column = data["temp"]

average_temp = round(temp_column.mean(), 3)
print(f"The average temperature was {average_temp}")

max_temp = temp_column.max()
print(f"The highest temperature was {max_temp}ºC")

hottest_day = data[data.temp == max_temp].day.to_list()[0]
print(f"The hottest day was {hottest_day}")

max_temp_fahrenheit = int(max_temp) * 9 / 5 + 32
print(f"The highest temperature in Fahrenheit was {max_temp_fahrenheit}ºF")
