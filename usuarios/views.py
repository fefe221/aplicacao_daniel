from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from .models import CustomUser
from .forms import UserForm

class UserListView(LoginRequiredMixin, ListView):
    model = CustomUser
    template_name = 'usuarios/user_list.html'
    context_object_name = 'users'
    paginate_by = 20

    def get_queryset(self):
        qs = super().get_queryset().order_by('username')
        q = self.request.GET.get('q', '').strip()
        if q:
            qs = qs.filter(
                Q(username__icontains=q) |
                Q(first_name__icontains=q) |
                Q(last_name__icontains=q) |
                Q(email__icontains=q)
            )
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['q'] = self.request.GET.get('q', '')
        return ctx

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
