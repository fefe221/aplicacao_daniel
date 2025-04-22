from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView
)
from .models import Venda
from django import forms

class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['vendedor', 'descricao', 'valor']
        widgets = {
            'vendedor':  forms.Select(attrs={'class':'form-select'}),
            'descricao': forms.TextInput(attrs={'class':'form-control'}),
            'valor':     forms.NumberInput(attrs={'class':'form-control'}),
        }

class VendaListView(LoginRequiredMixin, ListView):
    model = Venda
    template_name = 'vendas/venda_list.html'
    context_object_name = 'vendas'

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
