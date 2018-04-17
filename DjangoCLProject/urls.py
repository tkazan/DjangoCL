"""DjangoCLProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from DjangoCLApp.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name="home"),
    url(r'^pizza$', pizza, name="pizza"),
    url(r'^num/(?P<min>\d+)/(?P<max>\d+)$', random_number, name="num"),
    url(r'^pizzas$', pizza_list, name="pizza_list"),
    url(r'^pizza2$', pizza2, name="pizza2"),
    url(r'^form$', form, name="form"),
    url(r'^post$', form, name="post"),
    url(r'^get$', get_by_get, name="get"),
]
