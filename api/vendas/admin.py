from django.contrib import admin

from .models.vendas import VendasModel
from .models.venda_servicos import VendaServicoModel
from .models.venda_produtos import VendaProdutoModel


admin.site.register(VendasModel)
admin.site.register(VendaServicoModel)
admin.site.register(VendaProdutoModel)
