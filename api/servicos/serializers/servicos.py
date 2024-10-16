from datetime import datetime

from rest_framework import serializers

from ..models.servicos import ServicoModel


class ServicoSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        dt_cadastro = datetime.strftime(instance.dt_cadastro, "%d/%m/%Y - %H:%M")
        dt_alteracao = datetime.strftime(instance.dt_alteracao, "%d/%m/%Y - %H:%M")

        return {
            "id": instance.id,
            "ds_nome": instance.ds_nome,
            "ds_descricao": instance.ds_descricao,
            "nu_valor_unitario": instance.nu_valor_unitario,
            "dt_cadastro": dt_cadastro,
            "dt_alteracao": dt_alteracao,
        }

    class Meta:
        model = ServicoModel
        fields = "__all__"
