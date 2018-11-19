from django.shortcuts import render
from django.views import generic
from django.core import serializers
from atlas.models import Ship, Type, City, Country, Builder, Register, Status, Use, Owner

def index(request):
    static_ships_json = serializers.serialize("json", Ship.objects.all().filter(fleetmon__isnull=True), fields=("name", "type", "year_built", "city", "country", "lat", "lon", "slug"), use_natural_foreign_keys=True)
    active_ships_json = serializers.serialize("json", Ship.objects.all().filter(fleetmon__isnull=False), fields=("name", "fleetmon", "type", "year_built", "slug"), use_natural_foreign_keys=True)
    context = {"static_ships_json": static_ships_json, "active_ships_json": active_ships_json,}
    return render(request, "index.html", context,)

class ShipDetailView(generic.DetailView):
    model = Ship

class ShipListView(generic.ListView):
    model = Ship

class TypeDetailView(generic.DetailView):
    model = Type

class CityDetailView(generic.DetailView):
    model = City

class CountryDetailView(generic.DetailView):
    model = Country

class BuilderDetailView(generic.DetailView):
    model = Builder

class RegisterDetailView(generic.DetailView):
    model = Register

class StatusDetailView(generic.DetailView):
    model = Status

class UseDetailView(generic.DetailView):
    model = Use

class OwnerDetailView(generic.DetailView):
    model = Owner
