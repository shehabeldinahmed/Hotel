from django.shortcuts import render
from django.views.generic import DetailView ,ListView
from . models import Property
# Create your views here.

class PropertyList(ListView):
    model =Property
   


class PropertyDetail(DetailView):
    model =Property    