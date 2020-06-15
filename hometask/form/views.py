from django.shortcuts import render
from .models import Tyre

def tyre_list(request):
 tyres = Tyre.objects.all()
 return render(request, 'index.html',  {'posts': tyres})
