from django.urls import path
from .views import (
    VendaListView, VendaCreateView,
    VendaUpdateView, VendaDeleteView
)

app_name = 'vendas'

urlpatterns = [
    path('',    VendaListView.as_view(),   name='list'),
    path('add/',    VendaCreateView.as_view(), name='add'),
    path('<int:pk>/edit/',   VendaUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', VendaDeleteView.as_view(), name='delete'),
]
