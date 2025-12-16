import requests

URL = "https://api.openweathermap.org/data/2.5/weather"

parameters = {
    "lat": 37.566536,       # 위도 (서울)
    "lon": 126.977966,      # 경도 (서울)
    "appid": "",  # 개인 API 키
    "exclude": "current,minutely,daily"
}
res = requests.get(url=URL, params=parameters)
res.raise_for_status()
data = res.json()
print(data)
# import csv
# with open("weather_data.csv", mode='r') as data_files:
#     data = csv.reader(data_files)
#     next(data)  # 첫 번째 줄(헤더) 건너뛰기
#     temperatures = []
#     for row in data:
#         temperatures.append(int(row[1]))
    
    # print(temperatures)

import pandas as pd
data = pd.read_csv("weather_data.csv")
# print(type(data))
data_dict = data.to_dict()
# print(data_dict)

temp_list = data["temp"].to_list()
average = sum(temp_list) / len(temp_list)
# print(len(temp_list))
temp_series = data.temp
max_temp = temp_series.max()
max_day_index = data[max_temp == data.temp]
print(temp_series.idxmax())
print(max_day_index)

monday = data[data.day == "Monday"]
monday_temp = int(monday.temp)
print(monday_temp)

# max_temp = data["temp"].idmax()

# Get Data in Columns
first = data.loc[:1]