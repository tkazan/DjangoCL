from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from random import randint

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


def random_number(request, min, max):
    num = randint(int(min), int(max))

    return HttpResponse('<h1>{}</h1>'.format(num))


def pizza_list(request):

    margharita = Pizza.objects.get(pk=1)
    prosciutto = Pizza.objects.get(pk=2)

    html = """
    <h1>Pizza</h1>
    <ol>
        <li>{} {} {}</li>
        <li>{} {} {}</li>
    </ol>
    """.format(margharita.name, margharita.description, margharita.prize,
               prosciutto.name, prosciutto.description, prosciutto.prize)

    return HttpResponse(html)


def pizza2(request):

    pizzas = Pizza.objects.all()

    response = HttpResponse()
    response.write('<ul>')

    for pizza in pizzas:
        response.write('<li>{}: {}, cena: {}zł</li>'.format
                       (pizza.name, pizza.description, pizza.prize))

    response.write('</ul>')

    return response


@csrf_exempt
def form(request):

    if request.method == 'GET':
        html = """
        <form method="POST" action="/post">
            <label> Imię
                <input type="text" name="name">
            </label><br/>
            <label> Nazwisko
                <input type="text" name="surname">
            </label><br/>
                <input type="submit" value="wyślij">     
        </form>
        """

        return HttpResponse(html)

    if request.method == 'POST':
        name = request.POST.get("name")
        surname = request.POST.get("surname")

        html = """
        name: {}, surname: {}
        """.format(name, surname)

        return HttpResponse(html)