from django.db import models


class ClienteModel(models.Model):
    ds_nome = models.CharField(max_length=100)
    nu_telefone = models.CharField(max_length=11, null=True, blank=True)
    ds_email = models.CharField(max_length=100, null=True, blank=True)
    ds_endereco = models.TextField(null=True, blank=True)
    dt_cadastro = models.DateTimeField(auto_now_add=True)
    dt_alteracao = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self) -> str:
        return self.ds_nome

    class Meta:
        app_label = "clientes"
        db_table = "clientes"
