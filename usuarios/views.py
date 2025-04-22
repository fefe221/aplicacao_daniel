from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView
)
from .models import CustomUser
from django import forms

class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'referral_parent']
        widgets = {
            'referral_parent': forms.Select(attrs={'class': 'form-select'}),
        }

class UserListView(LoginRequiredMixin, ListView):
    model = CustomUser
    template_name = 'usuarios/user_list.html'
    context_object_name = 'users'

class UserCreateView(LoginRequiredMixin, CreateView):
    model = CustomUser
    form_class = UserForm
    template_name = 'usuarios/user_form.html'
    success_url = reverse_lazy('usuarios:list')

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = UserForm
    template_name = 'usuarios/user_form.html'
    success_url = reverse_lazy('usuarios:list')

class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = CustomUser
    template_name = 'usuarios/user_confirm_delete.html'
    success_url = reverse_lazy('usuarios:list')
