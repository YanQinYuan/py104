from flask import Flask
from flask import request
from flask import render_template
import openweathermap as owm
app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def main():
    if request.method == 'POST':
        current = owm.CurrentWeather()
        daily = owm.DailyWeather()
        location = request.form['location'].strip()
        unit = request.form['unit']
        status = get_unit_status(unit)
        if request.form['submit'] == 'Search':
            if location:
                data_current = current.get_current_weather(location, unit)
                data_daily = daily.get_daily_weather(location, unit, 7)
                if (type(data_current) is dict) or (type(data_daily) is dict):
                    weather_basic = current.organize_basic_data(data_current)
                    weather_detail = current.organize_detail_data(data_current)
                    current.save_to_history(weather_basic, weather_detail)
                    weather_daily = daily.organize_data(data_daily)
                    return render_template('weather.html', imperial=status,
                                            basic=weather_basic, detail=weather_detail,
                                            daily=weather_daily)
                else:
                    error = data_current
                    return render_template('error.html', imperial=status, error=error)
            else:
                return render_template('index.html', imperial=status)
        elif request.form['submit'] == 'History':
            error = None
            history = owm.CurrentWeather().weather_history
            if history:
                return render_template('history.html', imperial=status, history=history)
            else:
                error = 'No history record found！'
                return render_template('error.html', imperial=status, error=error)
    else:
        submit = request.args.get('submit', '')
        unit = request.args.get('unit', '')
        status = get_unit_status(unit)
        if submit == 'Help':
            with open('README.md', encoding="utf-8") as file:
                text = file.readlines()
            return render_template('help.html', imperial=status, help=text)
        else:
            return render_template('index.html')


def get_unit_status(unit):
    status = ''
    if unit == 'imperial':
        status = 'checked'
    return status


if __name__ == "__main__":
    app.run(debug=True)
