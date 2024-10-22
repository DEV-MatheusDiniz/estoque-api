from datetime import datetime

from rest_framework import serializers

from ..models.venda_servicos import VendaServicoModel

from api.vendas.serializers.vendas import VendaSerializer
from api.servicos.serializers.servicos import ServicoSerializer


class VendaServicosSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        dt_cadastro = datetime.strftime(instance.dt_cadastro, "%d/%m/%Y - %H:%M")
        dt_alteracao = datetime.strftime(instance.dt_alteracao, "%d/%m/%Y - %H:%M")

        fk_venda = VendaSerializer(instance.fk_venda).data
        fk_servico = ServicoSerializer(instance.fk_servico).data

        return {
            "id": instance.id,
            "nu_quantidade": instance.nu_quantidade,
            "nu_valor_unitario": instance.nu_valor_unitario,
            "nu_subtotal": instance.nu_subtotal,
            "fk_venda": fk_venda,
            "fk_servico": fk_servico,
            "dt_cadastro": dt_cadastro,
            "dt_alteracao": dt_alteracao,
        }

    class Meta:
        model = VendaServicoModel
        fields = "__all__"
