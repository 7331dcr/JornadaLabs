from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import datetime

from .models. import Client, Operation

# Create your views here.
def index(request):
    return render(request, "manager/index.html")


def add_client(resquest):
    pass


def add_operation(request):
    pass


def report(request):
    pass


def reports(request):
    pass
