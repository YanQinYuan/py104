from flask import Flask,url_for, render_template, request
from weatherquery import get_weather
app = Flask(__name__)
history = []
q_result = {}
@app.route('/')
def index():
    city_query = request.args.get('city_query','')
    if city_query:
        # print(city_query)
        query_result = get_weather(city_query)
        history.append(q_result)
        print(city_query)
        query_result00 = ''
        query_result01 = ''
        query_result02 = ''
        # if query_result == '查询不到该城市天气信息，请输入正确的城市名称':
        # 	q_result.update({
        # 		'query_result' : query_result,
        # 		'city_query' : city_query
        # 		})
        # else:
        wea_data = query_result.split("|")
        print(wea_data)
        query_result00 = wea_data[0]
        query_result01 = wea_data[1]
        query_result02 = wea_data[2]
        print(query_result00)
        q_result.update({
            "query_result00" : query_result00,
            "query_result01" : query_result01,
            "query_result02" : query_result02,
            "city_query" : city_query
        })
        # print(q_result)
        return render_template('index.html', **q_result)
    else:
        return render_template('index.html')
@app.route('/help')
def show_help():
    return render_template('help.html')

@app.route('/history')
def show_history():
    q_result.update({
    	'history':history
    	})
    return render_template('index.html', **q_result)
