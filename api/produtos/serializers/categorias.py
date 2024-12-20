from datetime import datetime

from rest_framework import serializers

from ..models.categorias import ProdutoCategoriaModel


class ProdutoCategoriaSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        dt_cadastro = datetime.strftime(instance.dt_cadastro, "%d/%m/%Y - %H:%M")
        dt_alteracao = datetime.strftime(instance.dt_alteracao, "%d/%m/%Y - %H:%M")

        return {
            "id": instance.id,
            "ds_nome": instance.ds_nome,
            "dt_cadastro": dt_cadastro,
            "dt_alteracao": dt_alteracao,
        }

    class Meta:
        model = ProdutoCategoriaModel
        fields = "__all__"
