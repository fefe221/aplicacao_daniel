from django.contrib import admin
from .models import Venda

@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'vendedor', 'valor','quantidade', 'data')
    list_filter  = ('vendedor', 'data')
    search_fields= ('descricao', 'vendedor__username')
