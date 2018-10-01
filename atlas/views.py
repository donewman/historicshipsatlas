from django.shortcuts import render
from django.views import generic
from atlas.models import Ship

class ShipDetailView(generic.DetailView):
    model = Ship
