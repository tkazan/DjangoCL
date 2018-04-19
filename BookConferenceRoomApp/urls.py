from django.conf.urls import url
from BookConferenceRoomApp.views import *

app_name = 'book'
urlpatterns = [
    url(r'^$', index, name="home"),
    url(r'^room/(?P<id>(\d)+)$', room, name="room"),
    url(r'^room/new$', NewRoomView.as_view(), name="new-room"),
    url(r'^room/modify/(?P<id>(\d)+)$', ModifyView.as_view(), name="modify"),
    url(r'^room/delete/(?P<id>(\d)+)$', DeleteView.as_view(), name="delete"),
    url(r'^room/reservation/(?P<id>(\d)+)$', ReservationView.as_view(), name="reservation"),
    url(r'^search$', SearchView.as_view(), name="search"),

]