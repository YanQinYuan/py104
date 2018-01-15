# -*- coding: utf-8 -*-
from flask import Flask,url_for, render_template, request, redirect
from weatherquery import get_weather
# from flask_sqlalchemy import *
from database import get_city_weather, insert_data, update_weather,get_history, isExisted, add_user,register_check
from wtforms import Form, TextField,PasswordField,validators

# from datetime import datetime
app = Flask(__name__)

class LoginForm(Form):
    username = TextField("username",[validators.Required()])
    password = PasswordField("password",[validators.Required()])

@app.route("/register", methods=['GET','POST'])
def register():
    myForm = LoginForm(request.form)
    if request.method == "POST":
        username = myForm.username.data
        password = myForm.password.data
        print(username)
        if myForm.validate():
            if register_check(username):
                message_2 = "User is existed! please try another username!"
                return render_template('register.html', message=message_2,form=myForm)
            else:
                add_user(username, password)
                message_1 = "register success!"
                return render_template('register.html', message=message_1,form=myForm)
        else:
            message = "invalid! register terminated!"
            return render_template('register.html', message=message,form=myForm)
    return render_template('register.html', form=myForm)

@app.route("/", methods=['GET'])
def index():
    return "Login successful!"

@app.route("/login", methods=['GET','POST'])
def login():
    myForm = LoginForm(request.form)
    if request.method =="get":
        username = myForm.username.data
        password = myForm.password.data
        if myForm.validate():
            if isExisted(username, password):
                message1 = "login success!"
                print(message1)
                return redirect("/")
            else:
                message = "User not existed or password is wrong!"
                return render_template('login.html', message=message,form=myForm)
        else:
            message = "Incompleted form! Login Failed!"
            return render_template('login.html', message=message, form=myForm)
    return render_template('login.html', form=myForm)
@app.route('/user_request')
def process_request():
    city_query = request.args.get('city')
    # print(city_query)
    # 开始计时。
    # if time>5min:
    # else:
    # time1 = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    if request.args.get('query')=="查询":
        try:
            weather_str = get_city_weather(city_query)
            print(weather_str + "database")
            # time0 = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            # print(time0)
            return render_template('index.html', weather_str=weather_str)
        except TypeError:
            try:
                day,location,weather,low,weather_str = get_weather(city_query)
                print(weather_str + "api")
                insert_data(day,location,weather,low)
                return render_template('index.html', weather_str=weather_str)
                # time0 = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                # print(time0)
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
