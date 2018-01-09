# -*- coding: utf-8 -*-
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
    input_info = input("请输入城市：")
    if input_info in ["help"]:
        print("""
        输入城市名，返回该城市天气;
        输入quit结束查询；
        输入help将得到帮助信息。
        输入history将展示历史查询信息""")
    elif input_info in weather_info.keys():
        print("{}的天气是{}".format(input_info,weather_info[input_info]))
        history_info = input_info + ":" + weather_info[input_info]
        print(history_info)
        history.append(history_info)

    elif input_info in ["quit"]:
        print("退出查询")
        pri_his(history)
        exit()
    elif input_info in ["histoty"]:
        print(history)
    elif input_info in ["shenzhen"]:
        print('wrong')
