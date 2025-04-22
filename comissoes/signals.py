# comissoes/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from vendas.models import Venda
from .models import CommissionRule, CommissionEntry

@receiver(post_save, sender=Venda)
def generate_commissions(sender, instance, created, **kwargs):
    if not created:
        return  # só dispara na criação

    seller = instance.vendedor
    valor  = instance.valor
    qty    = getattr(instance, 'quantidade', 1)

    # percorre até 5 níveis de referral_parent
    parent = seller.referral_parent
    for level in range(1, 6):
        if not parent:
            break
        try:
            rule = CommissionRule.objects.get(level=level)
        except CommissionRule.DoesNotExist:
            parent = parent.referral_parent
            continue

        if rule.calculation_type == 'percent' and rule.percent is not None:
            amount = (valor * rule.percent) / 100
        elif rule.calculation_type == 'fixed' and rule.fixed_amount is not None:
            amount = rule.fixed_amount * qty
        else:
            parent = parent.referral_parent
            continue

        CommissionEntry.objects.create(
            venda=instance,
            earner=parent,
            level=level,
            amount=amount
        )
        parent = parent.referral_parent
