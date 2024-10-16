from django.db import models


class ServicoModel(models.Model):
    ds_nome = models.CharField(max_length=100)
    ds_descricao = models.TextField()
    nu_valor = models.DecimalField(max_digits=10, decimal_places=2)
    dt_cadastro = models.DateTimeField(auto_now_add=True)
    dt_alteracao = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self) -> str:
        return self.ds_nome

    class Meta:
        app_label = "servicos"
        db_table = "servicos"
