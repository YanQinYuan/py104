from flask import Flask,url_for, render_template, request
from weatherquery.get_weather import get_weather_data

app = Flask(__name__)
history = []
q_result = {}
@app.route('/')
def index():
    city_query = request.args.get('','')
    if city_query:
        # print(city_query)
        query_result = get_weather_data(city_query)
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
