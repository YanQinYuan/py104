# -*- coding: utf-8 -*-
#for mac

weather_info = {}
with open('weather_info.txt','r',encoding = 'utf-8') as f:
    for i in f.readlines():
        data = i.split(',')
        weather_info.update({data[0]:data[-1]})
        # city = data[0]
        # weather = data[1]
        # weather_info[city] = weather
print("请输入需要查询的城市，如需帮助，请输入「help」")
history = []
def pri_his(history):
    for i in history:
        print(i)
while True:
    user_input = input("请输入需要查询的城市天气：")
    if weather_info.get(user_input):
        history_info = user_input + ":" + weather_info[user_input]
        history.append(history_info)
        print("{}：{}".format(user_input,weather_info[user_input]))
    elif user_input == 'history':
        pri_his(history)
    elif user_input == "quit":
        pri_his(history)
        break
    else:
        print("没有「{}」的天气信息".format(user_input))
        print("查询历史信息：")
