# coding: utf-8
import requests
from constant import API,LANGUAGE,KEY,UNIT
class get_weather(object):
	def __init__(self,api):
        self.api = API
        self.language = LANGUAGE
        self.key = KEY
        self.unit = UNIT
