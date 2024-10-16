from django.contrib import admin

from .models.compras import ComprasModel
from .models.compra_produto import CompraProdutoModel


admin.site.register(ComprasModel)
admin.site.register(CompraProdutoModel)
