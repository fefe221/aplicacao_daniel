# comissoes/urls.py
from django.urls import path
from .views import CommissionReportView

app_name = 'comissoes'

urlpatterns = [
    path('', CommissionReportView.as_view(), name='report'),
]
