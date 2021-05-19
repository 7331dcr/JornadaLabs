from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import datetime

from .models import Client, Currency, Operation


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
    if request.method == "POST":
        fee = 0.10

        # Validates client
        try:
            client = Client.objects.get(name=request.POST['client_name'])
        except Client.DoesNotExist:
            messages.error(request, f'Cliente não encontrado.')
            return HttpResponseRedirect(reverse('add_operation'))
        
        # Validates source_currency
        try:
            source_currency = Currency.objects.get(pk=request.POST['source_currency_id'])
        except Currency.DoesNotExist:
            messages.error(request, f'Moeda origem inválida.')
            return HttpResponseRedirect(reverse('add_operation'))

        # Validates target_currency
        try:
            target_currency = Currency.objects.get(pk=request.POST['target_currency_id'])
        except Currency.DoesNotExist:
            messages.error(request, f'Moeda destino inválida.')
            return HttpResponseRedirect(reverse('add_operation'))

        # Validates amount
        try:
            amount = float(request.POST['amount'])
        except ValueError:
            messages.error(request, f'Valor inválido.')
            return HttpResponseRedirect(reverse('add_operation'))

        # Converts currency
        sourceIndex = float(source_currency.indexed_value)
        targetIndex = float(target_currency.indexed_value)
        converted_amount = (targetIndex / sourceIndex) * amount
        fee_amount = converted_amount * fee
        total = converted_amount - fee_amount

        # Attempts to save to database
        try:
            new_operation = Operation(client=client, source_currency=source_currency,
            target_currency=target_currency, source_amount=amount, converted_amount=round(converted_amount, 2),
            fee_amount=round(fee_amount, 2), total=round(total, 2))
            new_operation.save()
            messages.success(request, f'Operação cadastrada com sucesso.')
            return HttpResponseRedirect(reverse('add_operation'))
        except Exception:
            messages.error(request, f'Não foi possível cadastrar a operação.')
            return HttpResponseRedirect(reverse('add_operation'))

    clients = Client.objects.all()
    currencies = Currency.objects.all()
    return render(request, "manager/add_operation.html", {
        'clients': clients,
        'currencies': currencies
    })


def report(request):
    pass


def reports(request):
    return render(request, "manager/reports.html")
