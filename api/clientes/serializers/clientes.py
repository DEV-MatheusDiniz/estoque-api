from datetime import datetime

from rest_framework import serializers

from ..models.clientes import ClienteModel


class ClienteSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        dt_cadastro = datetime.strftime(instance.dt_cadastro, "%d/%m/%Y - %H:%M")
        dt_alteracao = datetime.strftime(instance.dt_alteracao, "%d/%m/%Y - %H:%M")

        return {
            "id": instance.id,
            "ds_nome": instance.ds_nome,
            "nu_telefone": instance.nu_telefone,
            "ds_email": instance.ds_email,
            "ds_endereco": instance.ds_endereco,
            "dt_cadastro": dt_cadastro,
            "dt_alteracao": dt_alteracao,
        }

    class Meta:
        model = ClienteModel
        fields = "__all__"
