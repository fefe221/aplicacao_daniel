# comissoes/apps.py

from django.apps import AppConfig

class ComissoesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'comissoes'
    verbose_name = 'Comissões'

    def ready(self):
        # importa o módulo de signals para conectar os receivers
        import comissoes.signals
