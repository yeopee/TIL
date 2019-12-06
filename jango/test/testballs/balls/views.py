from django.shortcuts import render
from django.urls import path

# Create your views here.

def ball(request):

    return render(request, 'test.html')