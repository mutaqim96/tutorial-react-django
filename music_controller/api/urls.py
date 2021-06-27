# store smua urls yang local kepada app ni

from django.urls import path
from .views import RoomView

# main semua urls
urlpatterns = [
    path('home', RoomView.as_view()), 
]
