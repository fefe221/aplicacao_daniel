from django.urls import path
from .views import ArvoreIndicacoesView

app_name = 'arvore'

urlpatterns = [
    path('', ArvoreIndicacoesView.as_view(), name='minha_rede'),
]
