from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import datetime

from .models import Client, Operation

# Create your views here.
def index(request):
    return render(request, "manager/index.html")


def add_client(request):
    if request.method == 'POST':
        name = request.POST['name']

        if not name:
            messages.error(request, f'Nome inválido.')
            return render(request, "manager/add_client.html", status=400)

        # Checks if client's name is already registered
        try:
            Client.objects.get(name=name)
            messages.error(request, f'Cliente "{name}" já cadastrado.')
            return render(request, "manager/add_client.html", status=400)
        except Client.DoesNotExist:
            pass
        
        # Attempts to register new client to database
        try:
            new_client = Client(name=name)
            new_client.save()
            messages.success(request, f'Cliente "{name}" cadastrado com sucesso.')
            return render(request, "manager/add_client.html", status=201)
        except Exception:
            messages.error(request, f"Cadastro não efetuado.")
            return render(request, "manager/add_client.html", status=400)

    return render(request, "manager/add_client.html")


def add_operation(request):
    pass


def report(request):
    pass


def reports(request):
    pass
