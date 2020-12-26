from flask import Flask

import requests

app = Flask(__name__)

API_KEY = "3086802a05d4c3b89c5e2b71b778710c"

@app.route('/')
def index():
    name = "Hello World!"
    return name

@app.route('/<string:city>/<string:country>/')
def weather_by_city(country, city):
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = dict(
            q=city + "," + country,
            appid= API_KEY,
    )
    response = requests.get(url=url, params=params)
    data = response.json()
    return data

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
