import re


# result = {'results': [{'location': {'id': 'WS10730EM8EV', 'name': '深圳', 'country': 'CN', 'path': '深圳,深圳,广东,中国', 'timezone': 'Asia/Shanghai', 'timezone_offset': '+08:00'}, 'daily': [{'date': '2018-01-06', 'text_day': '小雨', 'code_day': '13', 'text_night': '阵雨', 'code_night': '10', 'high': '19', 'low': '15', 'precip': '', 'wind_direction': '无持续风向', 'wind_direction_degree': '', 'wind_speed': '10', 'wind_scale': '2'}, {'date': '2018-01-07', 'text_day': '阵雨', 'code_day': '10', 'text_night': '阵雨', 'code_night': '10', 'high': '18', 'low': '14', 'precip': '', 'wind_direction': '无持续风向', 'wind_direction_degree': '', 'wind_speed': '10', 'wind_scale': '2'}, {'date': '2018-01-08', 'text_day': '阵雨', 'code_day': '10', 'text_night': '阵雨', 'code_night': '10', 'high': '17', 'low': '7', 'precip': '', 'wind_direction': '无持续风向', 'wind_direction_degree': '', 'wind_speed': '15', 'wind_scale': '3'}], 'last_update': '2018-01-06T18:00:00+08:00'}]}
# result = str(result)

# re_temp = re.compile(r"code_day': '(.*)',")
# data_temp = re_temp.match('result')
# print(data_temp)

result = 'siw天气：「14」。。psasd'
# 提取14

re_pa = re.match(r'[0-9]+','siw天气：「14」。。psasd')
print(re_pa)