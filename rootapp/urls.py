from django.urls import path
from . import views
from django.http import HttpResponse
from django.shortcuts import render
from rootapp import views  
from calculatorapp import views

urlpatterns = [
    path('',views.root,name='root')
]