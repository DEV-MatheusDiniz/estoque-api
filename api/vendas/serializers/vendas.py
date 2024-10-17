from datetime import datetime

from rest_framework import serializers

from ..models.vendas import VendasModel

from api.clientes.serializers.clientes import ClienteSerializer


class VendaSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        if instance.dt_venda:
            dt_venda = datetime.strftime(instance.dt_venda, "%d/%m/%Y - %H:%M")
        else:
            dt_venda = ""

        dt_cadastro = datetime.strftime(instance.dt_cadastro, "%d/%m/%Y - %H:%M")
        dt_alteracao = datetime.strftime(instance.dt_alteracao, "%d/%m/%Y - %H:%M")

        fk_cliente = ClienteSerializer(instance.fk_cliente).data
        fk_funcionario = instance.fk_funcionario.username

        return {
            "id": instance.id,
            "dt_venda": dt_venda,
            "nu_valor_total": instance.nu_valor_total,
            "fk_cliente": fk_cliente,
            "fk_funcionario": fk_funcionario,
            "bo_finalizado": instance.bo_finalizado,
            "dt_cadastro": dt_cadastro,
            "dt_alteracao": dt_alteracao,
        }

    class Meta:
        model = VendasModel
        fields = "__all__"
