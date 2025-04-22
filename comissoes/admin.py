from django.contrib import admin
from .models import CommissionRule, CommissionEntry

@admin.register(CommissionRule)
class RuleAdmin(admin.ModelAdmin):
    list_display = ('level', 'calculation_type', 'percent', 'fixed_amount')

@admin.register(CommissionEntry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('venda', 'earner', 'level', 'amount', 'created_at')
    list_filter  = ('level', 'earner')
