# -*- coding: utf-8 -*-
#for mac

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
    elif input_info in ["quit"]:
        print("退出查询")
        pri_his(history)
        exit()
    elif input_info in ["histoty"]:
        print(history)
    elif input_info in ["shenzhen"]:
        print('wrong')
    else:
        
