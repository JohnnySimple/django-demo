from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("You know how we do it. Let's go to the mars🚀")