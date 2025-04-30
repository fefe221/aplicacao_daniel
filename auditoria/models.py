from django.db import models
from django.contrib.auth import get_user_model

class Auditoria(models.Model):
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    acao = models.CharField(max_length=255)
    data_hora = models.DateTimeField(auto_now_add=True)
    caminho = models.CharField(max_length=255, blank=True, null=True)
    metodo = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f"{self.usuario} - {self.acao} - {self.data_hora:%d/%m/%Y %H:%M:%S}"
