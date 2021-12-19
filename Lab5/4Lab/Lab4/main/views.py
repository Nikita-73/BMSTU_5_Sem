from django.shortcuts import render
from .models import IceCream

def index(request):
    return render(request, 'main/index.html')


def cream(request):
    return render(request, 'main/cream.html')


def ice_cr(request):
    return render(request, 'main/ice_cr.html')


def dari_ice_cr(request):
    return render(request, 'main/dari_ice_cr.html')


def sherbet(request):
    return render(request, 'main/sherbet.html')

def cost(request):
    iceCream = IceCream.objects.all()
    return render(request, 'main/cost.html',  {'title': 'Glavna', 'iceCream': iceCream})






