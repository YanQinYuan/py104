# -*- coding: utf-8 -*-
import requests
import re
def get_weather(input_info):
	history = []
	if input_info != 'history'
		API = "https://api.seniverse.com/v3/weather/daily.json"
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
		# print(daily)
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
		# 后日天气
		day2 = daily[2].get('text_day')
		night2 = daily[2].get('text_night')
		low2 = daily[2].get('low')
		high2 = daily[2].get('high')
		wind = daily[2].get('wind_direction')
		after_tom = "\n后天天气预报：\n"+location+"白天：{}\n夜晚：{}\n气温：{}～{}\n风向：{}".format(day2,night2,low2,high2,wind)
		# 添加历史
		print(today+'\n'+tomorrow+'\n'+after_tom)


def pri_his(history):
    for i in history:
        print(i)
history = []

while True:
    input_info = input("请输入需要查询的城市，如需帮助，请输入「help」：")
    if input_info in ["help"]:
        print("""
        输入城市名，返回该城市天气;
        输入quit结束查询；
        输入help将得到帮助信息。
        输入history将展示历史查询信息""")
    elif input_info in ["quit"]:
        print("退出查询")
        pri_his(history)
        exit()
    elif input_info in ["histoty"]:
        print(history)
    else:
    	get_weather(input_info)
    	history.append(today)
