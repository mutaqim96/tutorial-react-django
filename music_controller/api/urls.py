# store smua urls yang local kepada app ni

from django.urls import path
from .views import main

# main semua urls
urlpatterns = [
    path('', main)
]
