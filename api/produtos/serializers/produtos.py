from datetime import datetime

from rest_framework import serializers

from ..models.produtos import ProdutoModel

from .categorias import ProdutoCategoriaSerializer


class ProdutoSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        dt_cadastro = datetime.strftime(instance.dt_cadastro, "%d/%m/%Y - %H:%M")
        dt_alteracao = datetime.strftime(instance.dt_alteracao, "%d/%m/%Y - %H:%M")

        fk_categoria = ProdutoCategoriaSerializer(instance.fk_categoria).data

        return {
            "id": instance.id,
            "ds_nome": instance.ds_nome,
            "nu_valor_unitario": instance.nu_valor_unitario,
            "nu_quantidade_estoque": instance.nu_quantidade_estoque,
            "fk_tipo": instance.fk_tipo,
            "fk_categoria": fk_categoria,
            "dt_cadastro": dt_cadastro,
            "dt_alteracao": dt_alteracao,
        }

    class Meta:
        model = ProdutoModel
        fields = "__all__"
