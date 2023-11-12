from django.shortcuts import render
from EarthquakeApp.models import Earthquakes
def index(request):
    earthquakes = list(Earthquakes.objects.values('date','time','latitude','longitude','depth','magnitude'))
    context = {'earthquakes': earthquakes}
    return render(request, 'index.html', context)

def likelihood(request):
    earthquakes = list(Earthquakes.objects.values('date', 'time', 'latitude', 'longitude', 'depth', 'magnitude'))
    context = {'earthquakes': earthquakes}
    return render(request, 'earthquake_likelihood.html',context)