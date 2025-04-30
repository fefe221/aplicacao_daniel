from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView
)
from .models import Venda
from django import forms
from django.utils.timezone import datetime
from django.db.models import Q


class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['vendedor', 'descricao', 'valor', 'quantidade']
        widgets = {
            'vendedor':  forms.Select(attrs={'class': 'form-select'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control'}),
            'valor':     forms.NumberInput(attrs={'class': 'form-control'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
        }


class VendaListView(LoginRequiredMixin, ListView):
    model = Venda
    template_name = 'vendas/venda_list.html'
    context_object_name = 'vendas'

    def get_queryset(self):
        qs = super().get_queryset().select_related('vendedor').order_by('-id')
        q = self.request.GET.get('q', '').strip()
        data = self.request.GET.get('data', '').strip()

        if q:
            qs = qs.filter(
                Q(descricao__icontains=q) |
                Q(vendedor__first_name__icontains=q) |
                Q(vendedor__last_name__icontains=q)
            )
        if data:
            try:
                date_obj = datetime.strptime(data, '%Y-%m-%d').date()
                qs = qs.filter(data__date=date_obj)
            except ValueError:
                pass  # ignora se a data estiver inválida

        return qs

class VendaCreateView(LoginRequiredMixin, CreateView):
    model = Venda
    form_class = VendaForm
    template_name = 'vendas/venda_form.html'
    success_url = reverse_lazy('vendas:list')

class VendaUpdateView(LoginRequiredMixin, UpdateView):
    model = Venda
    form_class = VendaForm
    template_name = 'vendas/venda_form.html'
    success_url = reverse_lazy('vendas:list')

class VendaDeleteView(LoginRequiredMixin, DeleteView):
    model = Venda
    template_name = 'vendas/venda_confirm_delete.html'
    success_url = reverse_lazy('vendas:list')
