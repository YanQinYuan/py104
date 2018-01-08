# encoding='utf-8'
weather = {}
filepath = 'weather_info.txt'
def get_weather(filepath):
    with open(filepath,encoding='utf-8') as f:
        for weather_data in f.readlines():
            data = weather_data.strip().split(",")
            weather[data[0]] = data[1]
        # print(weather)

if __name__ == '__main__':
    input_info = input("请输入城市：")
    get_weather(filepath)
    while True:
        try:
            input_info in weather.keys()
            print(input_info + ':' + weather[input_info])
        except KeyError:
            print("没有该城市天气信息")
            return Falsec
