from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse

from .models import *


# Create your views here.


def index(request):

    rooms = Room.objects.all()

    ctx = {
        'rooms': rooms,
    }

    return render(request, 'Book/index.html', ctx)


def room(request, id):
    id = int(id)
    room = Room.objects.get(pk=id)
    if room.projector == True:
        projector = "TAK"
    else:
        projector = "NIE"

    ctx = {
        "room": room,
        "projector": projector,
    }
    return render(request, 'Book/room.html', ctx)




