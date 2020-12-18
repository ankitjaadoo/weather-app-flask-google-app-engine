from datetime import datetime
import os
import pytz
import requests
import math

API_KEY = '45e9a8d3c1ef81ad37f67fecb6dba3d4'
API_URL = ('http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&appid={}')

def query_api(city):    
    try:        
        print(API_URL.format(city, API_KEY))        
        data = requests.get(API_URL.format(city, API_KEY)).json()    
    except Exception as exc:        
        print(exc)        
        data = None    
    return data

