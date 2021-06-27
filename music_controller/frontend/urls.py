from django.urls import path
from .views import index

# main semua urls
urlpatterns = [
  
    path('',index)
]