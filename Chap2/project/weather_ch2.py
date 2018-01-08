# -*- coding: utf-8 -*-
import requests
import re
def get_weather(location):
	history = []
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
	if result.status_code == 200:
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
		# today = "\n今天天气：\n"+location+"白天：{}\n夜晚：{}\n气温：{}～{}\n风向：{}".format(day0,night0,low0,high0,wind)
		today = f"""
			{location}今日天气：白天{day0}，夜晚{night0}，气温：{low0}~{high0}
		"""
		# 明天天气
		day1 = daily[1].get('text_day')# 今天天气情况,「0」表示今天
		night1 = daily[1].get('text_night')
		low1 = daily[1].get('low')
		high1 = daily[1].get('high')
		wind = daily[1].get('wind_direction')
		# tomorrow = "\n明天天气预报：\n"+location+"白天：{}\n夜晚：{}\n气温：{}～{}\n风向：{}".format(day1,night1,low1,high1,wind)
		tomorrow = f"""
			{location}明天天气：白天{day1}，夜晚{night1}，气温：{low1}~{high1}
		"""
		# 后日天气
		day2 = daily[2].get('text_day')
		night2 = daily[2].get('text_night')
		low2 = daily[2].get('low')
		high2 = daily[2].get('high')
		wind = daily[2].get('wind_direction')
		# after_tom = "\n后天天气预报：\n"+location+"白天：{}\n夜晚：{}\n气温：{}～{}\n风向：{}".format(day2,night2,low2,high2,wind)
		after_tom = f"""
			{location}后天天气: 白天{day2}，夜晚{night2}，气温：{low2}~{high2}
		"""
		print(today,tomorrow,after_tom)
		# 添加历史
		# history.append([today,tomorrow,after_tom])
		# print(today+'\n'+tomorrow+'\n'+after_tom)
		# return history

def pri_his(history):
    for i in history:
        print(i)

def chat_weather():
	history = []
	print(history)
	while True:
	    input_info = input("请输入需要查询的城市，如需帮助，请输入「help」：")
		# history.append(input_info)
	    if input_info in ["help"]:
	        print("""
	        输入城市名，返回该城市天气;
	        输入quit结束查询；
	        输入help将得到帮助信息。
	        输入history将展示历史查询信息""")
	    elif input_info in ["quit"]:
	        print("退出查询")
	        exit()
	    elif input_info in ["history"]:
	        print(history)
	    else:
	    	get_weather(input_info)
if __name__ == '__main__':
	chat_weather()
