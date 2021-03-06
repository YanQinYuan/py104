import requests
from constant import GOOGLE_TZ, KEY, LANGUAGE, TIMEOUT


class TZ():
    def __init__(self):
        self.api = GOOGLE_TZ
        self.language = LANGUAGE
        self.key = KEY
        self.timeout = TIMEOUT

    def get_location_timestamp(self, timestamp, location):
        '''get current weather data from open weather map API,
        return the response data'''
        error = None
        params = {'location': location, 'timestamp': timestamp, 'language': self.language, 'key': self.key}
        try:
            r = requests.get(self.api, params=params, timeout=self.timeout)
            if r.status_code == requests.codes.ok:
                data = r.json()
                dstOffset = data['dstOffset']
                rawOffset = data['rawOffset']
                location_timestamp = timestamp + dstOffset + rawOffset
                return location_timestamp
            else:
                error = '访问Google Time Zone API失败!'
                return error
        except (requests.Timeout, requests.ConnectionError):
            error = '网络异常或者OpenWeatherMap API连接超时!'
            return error
