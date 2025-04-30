from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Auditoria
from django.db.models import Q
from datetime import datetime

class AuditoriaListView(LoginRequiredMixin, ListView):
    model = Auditoria
    template_name = 'auditoria/auditoria_list.html'
    context_object_name = 'registros'

    def get_queryset(self):
        qs = super().get_queryset().select_related('usuario')
        usuario = self.request.GET.get('usuario', '')
        data = self.request.GET.get('data', '')

        if usuario:
            qs = qs.filter(usuario__username__icontains=usuario)
        if data:
            try:
                data_obj = datetime.strptime(data, '%Y-%m-%d')
                qs = qs.filter(data_hora__date=data_obj.date())
            except ValueError:
                pass

        return qs.order_by('-data_hora')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['usuario'] = self.request.GET.get('usuario', '')
        ctx['data'] = self.request.GET.get('data', '')
        return ctx
