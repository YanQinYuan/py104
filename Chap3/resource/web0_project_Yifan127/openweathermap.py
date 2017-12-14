import requests
from datetime import datetime
import time
import calendar
from constant import OWM_CURRENT_API, OWM_DAILY_API, APPID, LANG, METRIC, IMPERIAL, TIMEOUT
from googletz import TZ


class OpenWeatherMap(object):
    def __init__(self, api):
        self.api = api
        self.lang = LANG
        self.appid = APPID
        self.timeout = TIMEOUT

    def get_request(self, params):
        '''get current weather data from open weather map API,
        return the response data'''
        data = {}
        error = None
        try:
            r = requests.get(self.api, params=params, timeout=self.timeout)
            if r.status_code == requests.codes.ok:
                data = r.json()
                return data
            else:
                error = 'Cannot access OpenWeatherMap API!'
                return error
        except (requests.Timeout, requests.ConnectionError):
            error = 'Network problem Or Timeout!'
            return error

    def set_display_unit(self, unit):
        '''set unit of measure when print weather information'''
        units = {}
        if unit == IMPERIAL:
            temperature_unit = '\u00b0F'
            wind_unit = 'miles/hour'

        if unit == METRIC:
            temperature_unit = '\u00b0C'
            wind_unit = 'meter/sec'

        units['temperature'] = temperature_unit
        units['wind'] = wind_unit

        return units

    def deg_to_direction(self, deg):
        '''convert wind degree to compass direction'''
        direction = ['N', 'NNE', 'NE', 'ENE',
                     'E', 'ESE', 'SE', 'SSE',
                     'S', 'SSW', 'SW', 'WSW',
                     'W', 'WNW', 'NW', 'NNW']
        value = int((deg / 22.5) + 0.5)
        return direction[value % 16]

    def get_location_datetime(self, coord, timestamp):
        '''calculate location local datetime'''
        location = '{:f}, {:f}'.format(coord['lat'], coord['lon'])
        utc_timestamp = timestamp + time.altzone

        tz = TZ()
        location_timestamp = tz.get_location_timestamp(utc_timestamp, location)
        if type(location_timestamp) is int:
            return location_timestamp
        else:
            return timestamp

    def timestamp_to_datetime(self, timestamp):
        '''convert timestamp to string format datetime'''
        dt = datetime.fromtimestamp(timestamp)
        weekday = calendar.day_name[dt.weekday()]
        fmt = '%Y-%m-%d %H:%M:%S %z'
        dt = weekday + ' ' + dt.strftime(fmt)
        return dt

    def timestamp_to_time(self, timestamp):
        '''convert timestamp to string format time'''
        dt = datetime.fromtimestamp(timestamp)
        fmt = '%H:%M:%S'
        dt = dt.strftime(fmt)
        return dt

    def timestamp_to_dateString(self, timestamp):
        '''convert timestamp to string format date'''
        dt = datetime.fromtimestamp(timestamp)
        fmt = '%Y-%m-%d'
        date = dt.strftime(fmt)
        return date


class CurrentWeather(OpenWeatherMap):

    weather_history = {}

    def __init__(self):
        super().__init__(OWM_CURRENT_API)

    def get_current_weather(self, location, unit):
        '''This function send a request to get current weather information,
        then prints the data'''
        params = {'q': location, 'units': unit, 'lang': self.lang, 'appid': self.appid}
        data = self.get_request(params)
        if type(data) is dict:
            if location.lower().strip() == data['name'].lower().strip():
                data['unit'] = params['units']
                return data
            else:
                error = 'Cannot find city: {0}!'.format(location)
                return error
        else:
            return data

    def organize_full_data(self, weather_basic, weather_detail):
        weather = weather_basic.copy()
        weather.update(weather_detail)
        return weather

    def save_to_history(self, weather_basic, weather_detail):
        if weather_basic:
            self.weather_history[weather_basic['location']] = {'basic': weather_basic,
                                                               'detail': weather_detail}

    def organize_basic_data(self, data):
        weather = {}
        if data:
            units = self.set_display_unit(data['unit'])

            weather['location'] = data['name']
            weather['description'] = data['weather'][0]['description']
            weather['icon'] = 'http://openweathermap.org/img/w/{0}.png'.format(data['weather'][0]['icon'])
            weather['temperature'] = str(round(data['main']['temp'])) + units['temperature']
            location_timestamp = self.get_location_datetime(data['coord'], data['dt'])
            weather['datetime'] = self.timestamp_to_datetime(location_timestamp)
        return weather

    def organize_detail_data(self, data):
        weather = {}
        if data:
            units = self.set_display_unit(data['unit'])

            weather['Pressure'] = str(int(data['main']['pressure'])) + 'hPa'
            weather['Humidity'] = str(data['main']['humidity']) + '%'

            if 'deg' in data['wind']:
                weather['Wind Direction'] = self.deg_to_direction(data['wind']['deg'])
            else:
                weather['Wind Direction'] = ''

            weather['Wind Speed'] = str(round(data['wind']['speed'])) + units['wind']
            weather['Clouds'] = str(data['clouds']['all']) + '%'

            location_sunrise = self.get_location_datetime(data['coord'], data['sys']['sunrise'])
            location_sunset = self.get_location_datetime(data['coord'], data['sys']['sunset'])
            weather['Sunrise'] = self.timestamp_to_time(location_sunrise)
            weather['Sunset'] = self.timestamp_to_time(location_sunset)

            if 'rain' in data:
                weather['Rain'] = str(data['rain']['3h']) + 'mm'
            else:
                weather['Rain'] = 0

            if 'snow' in data:
                weather['Snow'] = str(data['snow']['3h']) + 'mm'
            else:
                weather['Snow'] = 0

        return weather


class DailyWeather(OpenWeatherMap):
    def __init__(self):
        super().__init__(OWM_DAILY_API)

    def get_daily_weather(self, location, unit, cnt):
        '''This function sends a request to get daily forecast weather information,
        then prints the data'''
        params = {'q': location, 'units': unit, 'cnt': cnt, 'lang': self.lang, 'appid': self.appid}
        data = self.get_request(params)
        if data:
            if location.lower().strip() == data['city']['name'].lower().strip():
                data['unit'] = params['units']
                return data
            else:
                error = 'Cannot find city: {0}!'.format(location)
                return error
        else:
            return data

    def organize_data(self, data):
        weather = {}
        if data:
            weather['location'] = data['city']['name']
            units = self.set_display_unit(data['unit'])
            coord = data['city']['coord']
            if 'list' in data:
                daily = data['list']
            elif 'List' in data:
                daily = data['List']
            for day in daily:
                location_timestamp = self.get_location_datetime(coord, day['dt'])
                weekday = calendar.day_abbr[datetime.fromtimestamp(location_timestamp).weekday()]
                weather[weekday] = {}
                weather[weekday]['description'] = day['weather'][0]['description']
                weather[weekday]['icon'] = 'http://openweathermap.org/img/w/{0}.png'.format(day['weather'][0]['icon'])
                weather[weekday]['temperature_min'] = str(round(day['temp']['min'])) + units['temperature']
                weather[weekday]['temperature_max'] = str(round(day['temp']['max'])) + units['temperature']

        return weather
