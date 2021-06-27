from django.shortcuts import render
# Import httpresponse untuk bolehkan kita respond once receive request
from django.http import  HttpResponse

# Create your views here.
# write semua endpoint cth www.../apa2
# location on webserver 
def main(request):
  return HttpResponse("Hello")