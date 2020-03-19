from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

# Create your views here.
def index(request):
    url = "https://indianrailways.p.rapidapi.com/findstations.php"
    

    headers = {
     'x-rapidapi-host': "indianrailways.p.rapidapi.com",
     'x-rapidapi-key': "d11f0c1093msha9758c8c9938847p1281c1jsn8784017c8bf9"
     }

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()
    cities = City.objects.all()
    city = cities.last()

    r = requests.request("GET", url, headers=headers, params={"station": city } ).json()
    Names=[]
    Codes=[]
    for i in range(0,len(r['stations'])):
        Names.append(r['stations'][i]['stationName'])
        Codes.append(r['stations'][i]['stationCode'])

    station_info={}

    for i in range(0,len(r['stations'])):
        station_info[Names[i]] = Codes[i]

    context ={'station_info' : station_info, 'form' : form, 'city' : city}

    return render(request, 'station.html',context)