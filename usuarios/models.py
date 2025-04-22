from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """
    Extensão do User padrão do Django.
    referral_parent: usuário que o indicou (para futura comissão).
    """
    referral_parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='referrals',
        verbose_name='Usuário Indicador'
    )

    def __str__(self):
        return self.get_full_name() or self.username
