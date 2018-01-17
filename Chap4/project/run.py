# -*- coding: utf-8 -*-
from flask import Flask,url_for, render_template, request, redirect
from weatherquery import get_weather
from database import get_city_weather, insert_data, update_weather,get_history, isExisted, add_user,register_check, create_table
from wtforms import Form, TextField,PasswordField,validators
import os
import sqlite3
from flask import session, g, abort, flash, escape
import hashlib
# from datetime import datetime
app = Flask(__name__)
app.config.from_object(__name__) # load config from this file , flaskr.py
# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'weather.db'),
    SECRET_KEY='e35d7f4348184ed6a9aa15adfdb8c6f0' # uuid.uuid4.hex
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv
def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db
# print(get_db)
@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
    print('Initialized the database.')
def encode_password(password):
    return hashlib.md5(('slat:weatherquery' + password).encode()).hexdigest()

def create_user(username, password):
    raw_password = encode_password(password)
    conn = sqlite3.connect("weather.db")
    with conn:
        cur = conn.cursor()
        sql_create = """INSERT INTO users (username, password) values("{}", "{}")
                     """.format(username, raw_password)
        cur.execute(sql_create)

@app.cli.command('initadmin')
def initadmin_command():
    """Initializes the database."""
    create_user("admin", "123456")
    print('Initialized the admin.')
def query_user(username):
    conn = sqlite3.connect("weather.db")
    with conn:
        cur = conn.cursor()
        sql_query = """SELECT * FROM users where username='{}' """.format(username)
        user = cur.execute(sql_query).fetchone()
        return user
    print(user)
@app.cli.command('queryadmin')
def queryadmin_command():
    """query_admin."""
    print(dict(query_user('admin')))

# add entry
@app.route('/register/', methods=['GET', 'POST'])
def user_register():
    context = {}
    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        re_password = request.form.get('re_password')
        if not username:
            error = '用户名不能为空'
        elif not password:
            error = '密码不能为空'
        elif password != re_password:
            error = '两次输入的密码不一致'
        elif query_user(username):
            error = '用户已存在'
        if error is None:
            create_user(username, password)
            return redirect(url_for('login'))
        else:
            context.update({
            'error':error,
            'username':username
            })
    return render_template('register.html', **context)
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    context = {}
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        if not username:
            error = '请输入用户名'
        else:
            user = query_user(username)
            if not user:
                error = '用户不存在'
            else:
                user_password = user[-1]
                if encode_password(password) != user_password:
                    error = '用户名或密码错误'
                else:
                    session['login'] = True
                    session['user'] = username
                    return redirect(url_for('query'))
        context.update({
        'error':error
        })
    return render_template('login.html', **context)

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session["login"] = False
    return redirect(url_for('login'))

# set the secret key.  keep this really secret:
# app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route('/', methods=['GET','POST'])
def query():
    city_query = request.args.get('city')
    username = session.get('user')
    if username:
        if request.args.get('query')=="查询":
            create_table()
            try:
                weather_str = get_city_weather(city_query)
                print(weather_str + "database")
                return render_template('index.html', weather_str=weather_str)
            except TypeError:
                day,location,weather,low,weather_str = get_weather(city_query)
                print(weather_str + "api")
                insert_data(day,location,weather,low)
                return render_template('index.html', weather_str=weather_str)
        elif request.args.get('history')=="历史":
            history = get_history()
            return render_template('index.html', history=history)
        elif request.args.get('help')=="帮助":
            help = "help"
            return render_template("index.html",help=help)
        elif request.args.get('update')=="更新":
            city = city_query.split(' ')[0]
            print(city + "1")
            update = city_query.split(' ')[1]
            print(city+"\n"+update)
            update_data = update_weather(city, update)
            print(update_data,"2")
            return render_template('index.html', update_data=update_data)
    return render_template('index.html')
# @app.route('/help')
# def show_help():
#     help_str = """
#     <p>help yourself</p>
#     """
#     return render_template('index.html',help = help_str)
#
# @app.route('/history')
# def show_history():
#     return render_template('query.html', history = history)
# class LoginForm(Form):
#     username = TextField("username",[validators.Required()])
#     password = PasswordField("password",[validators.Required()])
#
# @app.route("/register", methods=['GET','POST'])
# def register():
#     myForm = LoginForm(request.form)
#     if request.method == "POST":
#         username = myForm.username.data
#         password = myForm.password.data
#         print(username)
#         if myForm.validate():
#             if register_check(username):
#                 message_2 = "User is existed! please try another username!"
#                 return render_template('register.html', message=message_2,form=myForm)
#             else:
#                 add_user(username, password)
#                 message_1 = "register success!"
#                 return render_template('register.html', message=message_1,form=myForm)
#         else:
#             message = "invalid! register terminated!"
#             return render_template('register.html', message=message,form=myForm)
#     return render_template('register.html', form=myForm)

# @app.route("/", methods=['GET'])
# def index():
#     return "Login successful!"

# @app.route("/login", methods=['GET','POST'])
# def login():
#     myForm = LoginForm(request.form)
#     if request.method =="get":
#         username = myForm.username.data
#         password = myForm.password.data
#         if myForm.validate():
#             if isExisted(username, password):
#                 message1 = "login success!"
#                 print(message1)
#                 return redirect("/")
#             else:
#                 message = "User not existed or password is wrong!"
#                 return render_template('login.html', message=message,form=myForm)
#         else:
#             message = "Incompleted form! Login Failed!"
#             return render_template('login.html', message=message, form=myForm)
#     return render_template('login.html', form=myForm)
# @app.route('/fix/')
# def fix_data():
#     return render_template("fix.html")

if __name__ == '__main__':
    app.run(debug=True)
