from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    referral_parent = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.SET_NULL, related_name='indicados'
    )


    def get_full_name(self):
        return f"{self.first_name} {self.last_name}".strip() or self.username