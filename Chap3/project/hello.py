from flask import Flask,url_for, render_template, request
from weatherquery import get_weather
app = Flask(__name__)
@app.route('/')
def index():
	city_query = request.args.get('city_query','')
	print(city_query)
	query_result = get_weather(city_query)
	print(query_result)
    return render_template('index.html',query_result)

@app.route('/user')
def user():
    return render_template('user.html')
@app.route('/profile')
def show_user_profile():
    return render_template('profile.html')
# @app.route('/user/<username>')
# def show_user_profile(username):
#     return 'User %s' % username
#
# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     return 'Post %d' % post_id
#
# @app.route('/')
# def index(): pass
#
# @app.route('/login')
# def login(): pass
#
# @app.route('user/<username>')
# def profile(username): pass
#
# with app.test_request_context():
#     print url_for('index')
#     print url_for('login')
#     print url_for('login',next='/')
#     print url_for('profile',username='John Doe')
