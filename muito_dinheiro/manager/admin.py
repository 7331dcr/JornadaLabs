from django.contrib import admin

# Register your models here.
from .models import Client, Operation

admin.site.register(Client)
admin.site.register(Operation)
