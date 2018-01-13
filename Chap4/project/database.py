# coding: utf-8
# 创建数据库，日期，城市，天气，温度
# 存储天气数据
# 根据城市名，得到天气数据
# 数据库历史信息显示功能
# 更新数据库信息
# 用户输入城市名，输出改城市天气信息，若没有，则从api里搜索
# 将用户查询信息存入数据库
# 用户点击历史按钮，从数据库获取信息显示
# 用户手动更新数据库
# 数据库定时更新

import sqlite3 as ite
def create_table():
	conn = ite.connect('weather.db')
	with conn:
		cur = conn.cursor()
		cur.execute("DROP TABLE if exists weather")
		cur.execute("CREATE TABLE weather(day text,city text,weather text,temp text)")

def insert_data(day,city,weather,temp):
	conn = ite.connect('weather.db')
	with conn:
		cur = conn.cursor()
		cur.execute("INSERT INTO weather VALUES(?,?,?,?)",(day,city,weather,temp))

def get_city_weather(location):
	conn = ite.connect('weather.db')
	with conn:
		cur = conn.cursor()
		cur.execute('SELECT day,city,weather,temp from weather where city=:location',{"location": location})
		data = cur.fetchone()
	weather_str = f"""{data[0]},{data[1]}天气:{data[2]},气温:{data[3]}"""
	print(weather_str)
	return weather_str

def get_history():
	conn = ite.connect('weather.db')
	with conn:
		cur = conn.cursor()
		cur.execute('SELECT * from weather')
		history = cur.fetchall()
	# print(history)
	return history
def update_weather(location, weather):
	conn = ite.connect('weather.db')
	with conn:
		cur = conn.cursor()
		cur.execute('UPDATE weather SET weather=? where city=?',(weather, location))

if __name__ == '__main__':
	# insert_data("1月13号","天津","多云","-4")
	# get_history()
	update_weather("天津","没有草原")

