from django.shortcuts import render
from django.http import HttpResponse
from .models import Vuelo
# Create your views here.
def index(request):
    
    context = {'vuelos': Vuelo.objects.all()
               }
    return render(request, 'miPrimerApp/index.html', context)