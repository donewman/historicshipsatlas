from django.shortcuts import render
from django.views import generic
from django.core import serializers
from atlas.models import Ship

def index(request):
    static_ships = serializers.serialize("json", Ship.objects.all().filter(fleetmon__isnull=True))
    context = {"static_ships": static_ships,}
    return render(request, "index.html", context,)

class ShipDetailView(generic.DetailView):
    model = Ship

class ShipListView(generic.ListView):
    model = Ship
