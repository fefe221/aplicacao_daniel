# comissoes/views.py

from django.db.models import Sum
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.views.generic import ListView
from .models import CommissionEntry

class CommissionReportView(LoginRequiredMixin, ListView):
    model = CommissionEntry
    template_name = 'comissoes/report.html'
    context_object_name = 'entries'
    paginate_by = 10  # default para listagem detalhada

    def get_paginate_by(self, queryset):
        per_page = self.request.GET.get('per_page')
        if per_page and per_page.isdigit() and int(per_page) in (10, 20, 30):
            return int(per_page)
        return self.paginate_by

    def get_queryset(self):
        qs = CommissionEntry.objects.all() if self.request.user.is_staff \
             else CommissionEntry.objects.filter(earner=self.request.user)

        start = self.request.GET.get('start_date')
        end   = self.request.GET.get('end_date')
        if start:
            qs = qs.filter(venda__data__date__gte=start)
        if end:
            qs = qs.filter(venda__data__date__lte=end)

        return qs.order_by('-created_at')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        qs = self.get_queryset()

        # 1) resumo bruto (lista de dicts com 'earner__username' e 'total')
        summary_list = (
            qs.values('earner__username')
              .annotate(total=Sum('amount'))
              .order_by('-total')
        )

        # 2) paginar esse resumo
        per_page = self.get_paginate_by(qs)
        summary_paginator = Paginator(summary_list, per_page)
        summary_page = self.request.GET.get('summary_page')
        summary_page_obj = summary_paginator.get_page(summary_page)

        # 3) contexto
        ctx.update({
            'summary_page_obj': summary_page_obj,
            'summary':         summary_page_obj.object_list,
            'start_date':      self.request.GET.get('start_date', ''),
            'end_date':        self.request.GET.get('end_date',   ''),
            'per_page':        per_page,
            'per_page_options': [10, 20, 30],
        })
        return ctx
