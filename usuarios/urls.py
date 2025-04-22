from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('', views.UserListView.as_view(), name='list'),
    path('add/', views.UserCreateView.as_view(), name='add'),
    path('<int:pk>/edit/', views.UserUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', views.UserDeleteView.as_view(), name='delete'),
]
