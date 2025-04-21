from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'acessos'

urlpatterns = [
    # Rota raiz -> dashboard
    path('', views.dashboard, name='home'),

    # Login e Logout
    path('login/',
         auth_views.LoginView.as_view(template_name='acessos/login.html'),
         name='login'),
    path('logout/',
         auth_views.LogoutView.as_view(),
         name='logout'),
]
