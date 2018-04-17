from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
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
            <label>Płeć
                <select name="gender">
                    <option value="">Select...</option>
                    <option value="F">Female</option>
                    <option value="M">Male</option>
            </label>
            <label>Hobby
                <input type="checkbox", name="hobby", value="football">PIŁKA NOŻNA
                <input type="checkbox", name="hobby", value="music">MUZYKA
                <input type="checkbox", name="hobby", value="movies">FILMY
                <input type="checkbox", name="hobby", value="travels">PODRÓŻE
                <input type="checkbox", name="hobby", value="books">KSIĄŻKI
                <input type="checkbox", name="hobby", value="washing">ZMYWANIE
            </label>
                <input type="submit" value="wyślij">     
        </form>
        """

        return HttpResponse(html)

    if request.method == 'POST':
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        gender = request.POST.get("gender")
        hobbies = request.POST.getlist("hobby")

        html = """
        name: {}, surname: {}, gender: {}, hobbies: {}
        """.format(name, surname, gender, hobbies)

        return HttpResponse(html)


def get_by_get(request):
    name = request.GET.get("name")
    surname = request.GET.get("surname")

    return HttpResponse("User name is {} and surname is {}".format(name, surname))


# @csrf_exempt
# def form2(request):
#
#     if request.method == "GET":
#         pizza1 = Pizza.objects.get(pk=1)
#         pizza2 = Pizza.objects.get(pk=2)
#         html = """
#         <form method="POST" action="/yourpizza">
#             <label>User name
#                 <input type="text" name="user_name">
#             </label><br/>
#             <label>Zamówienie
#                 <input type="checkbox", name="pizza", value="{}">{}
#                 <input type="checkbox", name="pizza", value="{}">{}
#             </label><br/>
#             <label>Dostawa
#                 <select name="delivery">
#                     <option value="">Select delivery...
#                     <option value="home">Home
#                     <option value="local">Local
#             </label>
#             <br/>
#             <input type="submit" value="wyślij">
#
#         </form>
#         """.format(pizza1, pizza1, pizza2, pizza2)
#
#         return HttpResponse(html)
#
#     if request.method == "POST":
#         user_name = request.POST.get("user_name")
#         pizza = request.POST.getlist("pizza")
#         delivery = request.POST.get("delivery")
#
#         return HttpResponse("User name: {}<br/> pizza: {}<br/> delivery: {}".format(
#             user_name, pizza, delivery
#         ))


@method_decorator(csrf_exempt, name='dispatch')
class FormView(View):

    def get(self, request):
        pizza1 = Pizza.objects.get(pk=1)
        pizza2 = Pizza.objects.get(pk=2)
        html = """
        <form method="POST" action="/yourpizza">
            <label>User name
                <input type="text" name="user_name">
            </label><br/>
            <label>Zamówienie
                <input type="checkbox", name="pizza", value="{}">{}
                <input type="checkbox", name="pizza", value="{}">{}
            </label><br/>
            <label>Dostawa
                <select name="delivery">
                    <option value="">Select delivery...
                    <option value="home">Home
                    <option value="local">Local
            </label>
            <br/>
            <input type="submit" value="wyślij">

        </form>
        """.format(pizza1, pizza1, pizza2, pizza2)

        return HttpResponse(html)

    def post(self, request):
        self.user_name = request.POST.get("user_name")
        self.pizza = request.POST.getlist("pizza")
        self.delivery = request.POST.get("delivery")

        return HttpResponse("User name: {}<br/> pizza: {}<br/> delivery: {}".format(
            self.user_name, self.pizza, self.delivery
        ))


