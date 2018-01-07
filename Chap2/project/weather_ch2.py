# -*- coding: utf-8 -*-
import requests
import re
API = "https://api.seniverse.com/v3/weather/daily.json"
location = input("please input city:")
LANGUAGE = "zh-Hans"
KEY = "ygnfdic5sis9nfpt"
UNIT = "c"
we_da = {}
result = requests.get(API, params={
    'key': KEY,
    'location': location,
    'language': LANGUAGE,
    'unit': UNIT
}, timeout=5)
rep_data = result.json()

# print(result)

results = rep_data.get('results')
daily = results[0].get('daily')
print(daily)
# 今天天气
day0 = daily[0].get('text_day')# 今天天气情况,「0」表示今天
night0 = daily[0].get('text_night')
low0 = daily[0].get('low')
high0 = daily[0].get('high')
wind = daily[0].get('wind_direction')
today = "今天天气：\n"+location+"白天：{}\n夜晚：{}\n气温：{}～{}\n风向：{}".format(day0,night0,low0,high0,wind)
# 明天天气
day1 = daily[1].get('text_day')# 今天天气情况,「0」表示今天
night1 = daily[1].get('text_night')
low1 = daily[1].get('low')
high1 = daily[1].get('high')
wind = daily[1].get('wind_direction')
tomorrow = "\n明天天气预报：\n"+location+"白天：{}\n夜晚：{}\n气温：{}～{}\n风向：{}".format(day1,night1,low1,high1,wind)
print(today)
print(tomorrow)