from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    """
    Página inicial após o login.
    Usuários não autenticados serão redirecionados para LOGIN_URL.
    """
    return render(request, 'acessos/dashboard.html')
