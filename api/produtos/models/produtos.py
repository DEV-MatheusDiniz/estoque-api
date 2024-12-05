from django.db import models

from .categorias import ProdutoCategoriaModel


class ProdutoModel(models.Model):
    TIPO_CHOICES = [
        ('GRANEL', 'Granel'),
        ('CONVENCIONAL', 'Convencional'),
    ]

    ds_nome = models.CharField(max_length=100)
    nu_valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    nu_quantidade_estoque = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    ds_tipo = models.CharField(max_length=12, choices=TIPO_CHOICES, default='Convencional')
    fk_categoria = models.ForeignKey(ProdutoCategoriaModel, on_delete=models.CASCADE)

    dt_cadastro = models.DateTimeField(auto_now_add=True)
    dt_alteracao = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    def __str__(self) -> str:
        return self.ds_nome

    class Meta:
        app_label = "produtos"
        db_table = "produtos"
