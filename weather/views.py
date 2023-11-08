from django.shortcuts import render
import json
import urllib.request


def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen(
            'https://api.openweathermap.org/data/2.5/weather?q=' + city +
            '&appid=34b4ef190acad907288419b1982aa2ba').read()
        json_data = json.loads(res)
        data = {
            "city" : city,
            "country_code": str(json_data['sys']['country']),
            "cordinate": str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
            "temp": str(json_data['main']['temp']),
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),

        }
    else:
        data = {}
    return render(request, 'index.html', data)
