# Register your models here.
from django.contrib import admin
from .models import Celular

class CelularAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')  # Inclui o campo id na listagem
    list_display_links = ['nome']

admin.site.register(Celular,CelularAdmin)
