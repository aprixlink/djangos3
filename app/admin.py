"""Archivo que configura la zona de administracion del app."""
from django.contrib import admin
from . models import File

admin.site.register(File)
