from django.http import HttpResponse
from django.shortcuts import render

from .models import *


# Create your views here.

def home(request):
    return HttpResponse('Hello World')

def pizza(request):

    pizzas = Pizza.objects.all()
    pizza_list = []

    for pizza in pizzas:
        pizza_list.append((pizza.name, pizza.description))

    return HttpResponse(pizza_list)