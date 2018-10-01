from django.shortcuts import render
from django.views import generic

class ShipDetailView(generic.DetailView):
    model = Ship
