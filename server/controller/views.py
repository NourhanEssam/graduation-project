from django.shortcuts import render
from django.http import HttpResponse
from controller.models import TrafficLight
import re

# Create your views here.
from server.settings import INSTALLED_APPS


def index(request):
    return HttpResponse("<h1>Hello Controller</h1>");