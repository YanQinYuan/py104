# -*- coding: utf-8 -*-
from flask import Flask,url_for, render_template, request
from weatherquery import get_weather
from flask_sqlalchemy import *
from database import get_city_weather, insert_data, update_weather,get_history

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user_request')
def process_request():
    city_query = request.args.get('city')
    # print(city_query)
    if request.args.get('query')=="查询":
        try:
            weather_str = get_city_weather(city_query)
            print(weather_str + "database")
            return render_template('index.html', weather_str=weather_str)
        except TypeError:
            try:
                day,location,weather,low,weather_str = get_weather(city_query)
                print(weather_str + "api")
                insert_data(day,location,weather,low) 
                return render_template('index.html', weather_str=weather_str)
            except KeyError:
                return render_template('404.html')
    elif request.args.get('history')=="历史":
        history = get_history()
        return render_template('index.html', history=history)
    elif request.args.get('help')=="帮助":
        help = "help"
        return render_template("index.html",help=help)
    elif request.args.get('update')=="更新": # 深圳 + 大雨
        city = city_query.split(' ')[0]
        print(city + "1")
        update = city_query.split(' ')[1]
        print(city+"\n"+update)
        update_data = update_weather(city, update)
        print(update_data,"2")
        return render_template('index.html', update_data=update_data)
# @app.route('/help/')
# def show_help():
#     help_str = """
#     <p>help yourself</p>
#     """
#     return render_template('index.html',help = help_str)

# @app.route('/history/')
# def show_history():
#     return render_template('index.html', history = history)

# @app.route('/fix/')
# def fix_data():
#     return render_template("fix.html")

if __name__ == '__main__':
    app.run(debug=True)