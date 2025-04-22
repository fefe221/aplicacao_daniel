# comissoes/models.py

from django.db import models
from django.conf import settings
from vendas.models import Venda


class CommissionRule(models.Model):
    """
    Define a % de comissão ou valor fixo por unidade por nível da árvore (1 a 5).
    """
    LEVEL_TYPE = [
        ('percent', 'Percentual'),
        ('fixed',   'Fixo por unidade'),
    ]

    level            = models.PositiveSmallIntegerField(unique=True)
    calculation_type = models.CharField(
        'Tipo',
        max_length=10,
        choices=LEVEL_TYPE,
        default='percent'
    )
    percent          = models.DecimalField(
        'Percentual',
        max_digits=5,
        decimal_places=2,
        blank=True,
        null=True,
        help_text="Ex: 5.00 para 5% (use apenas se tipo=percent)"
    )
    fixed_amount     = models.DecimalField(
        'Valor fixo por unidade',
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        help_text="Ex: 2.50 (use apenas se tipo=fixed)"
    )

    class Meta:
        ordering = ['level']
        verbose_name = 'Regra de Comissão'
        verbose_name_plural = 'Regras de Comissão'

    def __str__(self):
        return f"Nível {self.level}: {self.percent if self.calculation_type=='percent' else self.fixed_amount}"


class CommissionEntry(models.Model):
    """
    Salva cada comissão gerada por venda para cada usuário até o 5º nível.
    """
    venda      = models.ForeignKey(
        Venda,
        on_delete=models.CASCADE,
        related_name='commissions'
    )
    earner     = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='earned_commissions'
    )
    level       = models.PositiveSmallIntegerField()
    amount      = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Comissão'
        verbose_name_plural = 'Comissões'

    def __str__(self):
        return f"{self.earner.username} ganhou R${self.amount} (Nível {self.level})"
