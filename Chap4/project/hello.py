from flask import Flask,url_for, render_template, request
from weatherquery import get_weather
from flask_sqlalchemy import *

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# db.SQLALchemy(app)
# db.create_all()

history = []
q_result = {}

# class User(db.Model):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer,primary_key=True)
#     username = db.Column(db.String(80),unique=True,nullable=False)
#     email = db.Column(db.String(120),unique=True,nullable=False)
#
#     def __init__(self,username,email)
#     self.username = username
#     self.email = email
#
#     def __repr__(self):
#         return '<User %r>' % self.username

@app.route('/')
def index():
    city_query = request.args.get('city_query','')
    if city_query:
        # print(city_query)
        query_result = get_weather(city_query)
        if city_query not in history:
            history.append(city_query)
            history.append(query_result)
        q_result.update({
            "query_result" : query_result,
            "city_query" : city_query
        })
        return render_template('index.html', **q_result)
    else:
        return render_template('index.html')
@app.route('/help/')
def show_help():
    help_str = """
    <p>help yourself</p>
    """
    return render_template('index.html',help = help_str)

@app.route('/history/')
def show_history():
    return render_template('index.html', history = history)

@app.route('/fix/')
def fix_data():
    return render_template("fix.html")
#
# @app.route('adduser')
# def add_user():
#     user1 = User('ethan','ethan@example.com')
#     user2 = User('jack','jack@example.com')
#     user3 = User('guest','guest@example.com')
#
#     db.session.add(user1)
#     db.session.add(user2)
#     db.session.add(user3)
#
#     db.session.commit()
#     return "add successfully!"
#
