
from django.shortcuts import render
import requests

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=1e1cd8bd1630d4d2aeff9e0d1ee84b1d'
    city = 'Auckland'
    city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types

    weather = {
        'city': city,
        'temperature': city_weather['main']['temp'],
        'description': city_weather['weather'][0]['description'],
        'icon': city_weather['weather'][0]['icon']
    }

    context = {'weather': weather}

    return render(request, 'home.html', context) #returns the index.html template