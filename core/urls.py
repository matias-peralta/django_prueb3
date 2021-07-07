from django.urls import path,include
from .views import home

urlPatterns = [
    path('',home,name="home"),
    
]