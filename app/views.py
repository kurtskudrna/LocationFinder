from app.models import Location
from app.forms import findLocationForm
from django.shortcuts import redirect, render
from .forms import findLocationForm
from django.contrib import messages
import folium
import geocoder

# Create your views here.


def index(request):
    form = findLocationForm
    search = Location.objects.all().last()
    location = geocoder.osm(search)
    latitude = location.lat
    longitude = location.lng
    country = location.country

    if request.method == 'POST':
        form = findLocationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/')
    else:
        if country == None:
            messages.warning(request, 'Search entry not valid')
            search.delete()
            return redirect('/')

    map = folium.Map(location=(latitude, longitude), zoom_start=10)
    folium.Marker(
        location=[latitude, longitude],
        popup='Requested Location',
        icon=folium.Icon(color="blue"),
    ).add_to(map)
    map = map._repr_html_()

    context = {
        'map': map,
        'form': form
    }
    return render(request, 'app/index.html', context)
