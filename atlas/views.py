from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.views.generic.base import RedirectView
from django.core import serializers
from django.contrib.postgres.search import SearchVector
from atlas.models import Ship, Type, City, Country, Builder, Register, Status, Use, Owner
from atlas.forms import BasicSearchForm, AdvancedSearchForm

def index(request):
    static_ships_json = serializers.serialize("json", Ship.objects.all().filter(fleetmon__isnull=True), fields=("name", "type", "year_built", "city", "country", "status", "lat", "lon", "slug"), use_natural_foreign_keys=True)
    active_ships_json = serializers.serialize("json", Ship.objects.all().filter(fleetmon__isnull=False), fields=("name", "fleetmon", "type", "year_built", "slug"), use_natural_foreign_keys=True)
    context = {"static_ships_json": static_ships_json, "active_ships_json": active_ships_json,}

    return render(request, "index.html", context,)

class ShipListView(ListView):
    model = Ship

class SearchView(ListView):
    model = Ship
    def get_queryset(self):
        try:
            search_string = self.request.GET["keywords"]
            results = Ship.objects.annotate(
                search=(
                    SearchVector("name", "type__name", "city__name", "city__region", "country__name", "builder__name", "builder__city__name", "builder__city__region", "builder__country__name", "registers__name", "status__name", "uses__name", "owner__name", "former_names", "description")
                ),
            ).filter(search=search_string).distinct("pk")
            return results
        except KeyError:
            return Ship.objects.none()

class ShipDetailView(DetailView):
    model = Ship

class TypeDetailView(DetailView):
    model = Type

class CityDetailView(DetailView):
    model = City

class CountryDetailView(DetailView):
    model = Country

class BuilderDetailView(DetailView):
    model = Builder

class RegisterDetailView(DetailView):
    model = Register

class StatusDetailView(DetailView):
    model = Status

class UseDetailView(DetailView):
    model = Use

class OwnerDetailView(DetailView):
    model = Owner
