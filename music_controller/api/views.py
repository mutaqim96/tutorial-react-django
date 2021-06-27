from django.shortcuts import render
from rest_framework import generics
#boleh buat class yang inherit daripada generics api views.
from .serializers import RoomSerializer
from .models import Room

# Import httpresponse untuk bolehkan kita respond once receive request
# from django.http import  HttpResponse

# Create your views here.
# write semua endpoint cth www.../apa2
# location on webserver 
# def main(request):
#   return HttpResponse("<h1>Hello</h1>")

class RoomView(generics.CreateAPIView):
  queryset = Room.objects.all()
  serializer_class = RoomSerializer

