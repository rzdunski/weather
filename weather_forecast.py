from urllib2 import Request, urlopen, URLError
import json, datetime, pprint
from sys import argv
"""
documetation based on website
http://openweathermap.org/current
"""

script, city, API_Key = argv


request="http://api.openweathermap.org/data/2.5/weather?q=" + city+ "&units=metric&APPID=" + API_Key



def time_sunset(u):
    sunset = datetime.datetime.utcfromtimestamp(u)
    sunset = sunset.strftime('%H:%M')
    return sunset
    

def time_sunrise(u):
    sunrise = datetime.datetime.utcfromtimestamp(u)
    sunrise = sunrise.strftime('%H:%M')
    return sunrise

def js_data(request):
    try:
        response = urlopen(request)
        pogoda = response.read()
        js = json.loads(pogoda)
    except URLError, e:
        print 'No forecast for indicated city. Get error:', e
    return js
    
def data_weather(js):

    unix_sunset = js['sys']['sunset']
    unix_sunrise = js['sys']['sunrise']

    s_data = (
        "Sunrise: %s" % time_sunrise(unix_sunrise),
        "Sunset: %s" % time_sunset(unix_sunset),
        "Temperature:%s C" % js['main']['temp'],
	"Temperature max:%s C" % js['main']['temp_max'],
	"Temperature min:%s C" % js['main']['temp_min'],
        "Pressure: %s hPa" % js['main']['pressure'],
        "Wind speed: %s" % js['wind']['speed'],
        )
    
    return s_data

js = js_data(request)
s_data = data_weather(js)
print s_data
