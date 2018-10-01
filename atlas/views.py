from django.shortcuts import render

class ShipDetailView(generic.DetailView):
    model = Ship
