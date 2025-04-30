from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from usuarios.models import CustomUser

class ArvoreIndicacoesView(LoginRequiredMixin, TemplateView):
    template_name = 'arvore/arvore_indicacoes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        def build_tree(user):
            user_url = reverse('usuarios:update', args=[user.pk])
            children = CustomUser.objects.filter(referral_parent=user)
            return {
                "innerHTML": f"<a href='{user_url}'>{user.get_full_name() or user.username}</a>",
                "children": [build_tree(child) for child in children]
            }

        context['tree_data'] = build_tree(user)
        return context
