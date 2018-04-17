from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse


# Create your views here.


def index(request):

    ctx = {}

    return render(request, 'Book/index.html', ctx)
