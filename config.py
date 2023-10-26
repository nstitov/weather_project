from environs import Env

env = Env()
env.read_env()

USE_ROUNDED_COORDS = False
OPENWEATHER_API = env('OPENWEATHER_API_KEY')
OPENWEATHER_URL = ('https://api.openweathermap.org/data/2.5/weather?'
                   'lat={latitude}&lon={longitude}&'
                   'exclude=hourly,daily&'
                   'appid=' + OPENWEATHER_API + '&lang=ru&'
                   'units=metric')