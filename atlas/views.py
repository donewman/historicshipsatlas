from django.shortcuts import render
from django.views import generic
from atlas.models import Ship

def index(request):
    return render(request, 'index.html')

class ShipDetailView(generic.DetailView):
    model = Ship
