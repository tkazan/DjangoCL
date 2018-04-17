from django.conf.urls import url
from DjangoCLApp.views import *

app_name = 'training'
urlpatterns = [
    url(r'^$', home, name="home"),
    url(r'^pizza$', pizza, name="pizza"),
    url(r'^num/(?P<min>\d+)/(?P<max>\d+)$', random_number, name="num"),
    url(r'^pizzas$', pizza_list, name="pizza_list"),
    url(r'^pizza2$', pizza2, name="pizza2"),
    url(r'^form$', form, name="form"),
    url(r'^post$', form, name="post"),
    url(r'^get$', get_by_get, name="get"),
    url(r'^form2$', FormView.as_view(), name="form2"),
    # url(r'^yourpizza$', form2, name="yourpizza"),
    url(r'^yourpizza$', FormView.as_view(), name="yourpizza"),
    url(r'^index$', HomeView.as_view(), name="index"),
]