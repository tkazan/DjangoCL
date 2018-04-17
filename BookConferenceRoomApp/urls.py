from django.conf.urls import url
from BookConferenceRoomApp.views import *

app_name = 'book'
urlpatterns = [
    url(r'^$', index, name="home"),
    url(r'^room/(?P<id>(\d)+)$', room, name="room"),

]