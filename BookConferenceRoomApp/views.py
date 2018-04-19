from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from datetime import datetime

from .models import *

# Create your views here.

today = datetime.today().strftime('%Y-%m-%d')


def index(request):
    rooms = Room.objects.all()
    status = {}

    for room in rooms:
        if room.reservation_set.filter(date=today):
            status[room.id] = 'Zajęta'
        else:
            status[room.id] = 'Wolna'
        ctx = {
            'rooms': rooms,
            'status': status,
    }
    return render(request, 'Book/index.html', ctx)


def room(request, id):
    id = int(id)
    room = Room.objects.get(pk=id)
    reservations = room.reservation_set.filter(date__gte=today).order_by('date')
    if room.projector == True:
        projector = "TAK"
    else:
        projector = "NIE"
    ctx = {
        "room": room,
        "projector": projector,
        "reservations": reservations,
    }
    return render(request, 'Book/room.html', ctx)


class NewRoomView(View):

    def get(self, request):
        return render(request, 'Book/new_room.html')

    def post(self, request):
        try:
            name = request.POST.get("name")
            capacity = request.POST.get("capacity")
            projector = request.POST.get("projector")
            proj = True if projector == "True" else False

            Room.objects.create(name=name, capacity=capacity, projector=proj)
            return redirect("/bookconfroom/")

        except Exception as e:
            message = "Niepoprawne dane: {}".format(e)
            ctx = {
                "message": message,
            }
            return render(request, 'Book/new_room.html', ctx)


class ModifyView(View):

    def get(self, request, id):
        room = Room.objects.get(pk=id)
        ctx = {
            "room": room,
        }
        return render(request, 'Book/modify.html', ctx)

    def post(self, request, id):
        name = request.POST.get("name")
        capacity = request.POST.get("capacity")
        projector = True if request.POST.get('projector') else False
        room = Room.objects.get(pk=id)
        try:
            room.name = name
            room.capacity = capacity
            room.projector = projector
            room.save()
            return redirect("/bookconfroom/")
        except Exception as e:
            message = "Niepoprawne dane: {}".format(e)
            ctx = {
                "message": message,
                "room": room,
            }
            return render(request, 'Book/modify.html', ctx)


class DeleteView(View):

    def get(self, request, id):
        room = Room.objects.get(pk=id)
        ctx = {
            "room": room,
        }
        return render(request, 'Book/delete.html', ctx)

    def post(self, request, id):
        action = request.POST.get("submit")

        if action == "TAK":
            room = Room.objects.get(pk=id)
            room.delete()
        return redirect("/bookconfroom/")


class ReservationView(View):

    def get(self, request, id):
        room = Room.objects.get(pk=id)
        reservations = room.reservation_set.filter(date__gte=today).order_by('date')
        ctx = {
            "room": room,
            "reservations": reservations,
        }
        return render(request, 'Book/reservation.html', ctx)

    def post(self, request, id):
        room = Room.objects.get(pk=id)
        reservations = room.reservation_set.filter(date__gte=today).order_by('date')
        try:
            date = request.POST.get("date")
            comment = request.POST.get("comment")
            message = ""

            if room.reservation_set.filter(date=date):
                message = "Sala jest już zajęta w ten dzień"
            elif date < today:
                message = "Wybrana data nie może być z przeszłości"

            if (message == "Sala jest już zajęta w ten dzień"
                or message == "Wybrana data nie może być z przeszłości"):
                ctx = {
                    "room": room,
                    "reservations": reservations,
                    "message": message,
                }
                return render(request, 'Book/reservation.html', ctx)

            reservation = Reservation.objects.create(date=date, comment=comment)
            reservation.room.add(room)

        except Exception as e:
            message = "Niepoprawne dane: {}".format(e)
            ctx = {
                "message": message,
                "room": room,
                "reservations": reservations,
            }
            return render(request, 'Book/reservation.html', ctx)

        if room.projector == True:
            projector = "TAK"
        else:
            projector = "NIE"
        message = """Dziękujemy! Zarezerwowałeś salę: 
                     {} w dniu: {}""".format(room.name, date)
        ctx = {
            "room": room,
            "projector": projector,
            "reservations": reservations,
            "message": message,
        }
        return render(request, 'Book/room.html', ctx)


class SearchView(View):

    def get(self, request):
        room = request.GET.get("room")
        capacity = request.GET.get("capacity")
        date = request.GET.get("date")
        projector = True if request.GET.get('projector') else False

        if projector == True:
            proj = "TAK"
        else:
            proj = "NIE"

        ctx = {
            "room": room,
            "capacity": capacity,
            "date": date,
            "projector": proj,
        }
        return render(request, 'Book/search.html', ctx)





