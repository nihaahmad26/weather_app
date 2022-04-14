from django.shortcuts import render
import urllib.request 
import json
import os




def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        API_KEY = os.environ['API_KEY']
        source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=imperial&appid=' + API_KEY).read()
        list_of_data = json.loads(source)
        data = {
            "city": city,
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['main']['temp']),
            "feels_like": str(list_of_data['main']['feels_like']),
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            "main": str(list_of_data['weather'][0]['main']),
            "description":str(list_of_data['weather'][0]['description']),
            "icon": list_of_data['weather'][0]['icon'],
        }
        print(data)
    else:
        data = {}
    
    return render(request, "main/index.html", data)