from django.urls import path
from .views import UserListView, UserCreateView, UserUpdateView, UserDeleteView

# este app_name deve bater com o segundo elemento da tupla acima
app_name = 'usuarios'

urlpatterns = [
    path('',            UserListView.as_view(),   name='list'),
    path('new/',        UserCreateView.as_view(), name='create'),
    path('<int:pk>/edit/',   UserUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', UserDeleteView.as_view(), name='delete'),
]
