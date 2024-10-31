from rest_framework.views import APIView, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from ..models.vendas import VendasModel
from api.clientes.models.clientes import ClienteModel

from ..serializers.vendas import VendaSerializer


class VendasAPIView(APIView):
    permission_classes = (AllowAny, )

    def get(self, request, id=None, *args, **kwargs):
        if id:
            result = VendasModel.objects.filter(id=id)
        else:    
            result = VendasModel.objects.all()
        
        vendas_serializer = VendaSerializer(result, many=True).data

        return Response(vendas_serializer)

    def post(self, request, *args, **kwargs):
        funcionario = request.user

        requisicao = request.data

        cliente = ClienteModel.objects.get(id=requisicao["fk_cliente"])

        requisicao["fk_funcionario"] = funcionario
        requisicao["fk_cliente"] = cliente
        
        venda = VendasModel.objects.create(**requisicao)

        vendas_serializer = VendaSerializer(venda).data

        return Response(vendas_serializer)
    
    def delete(self, request, id):
        try:
            venda = VendasModel.objects.get(id=id)

            serializer = VendaSerializer(venda).data

            venda.delete()

            return Response(serializer)

        except VendasModel.DoesNotExist:
                    return Response(
                        {"error": "Venda não encontrada."},
                        status=status.HTTP_404_NOT_FOUND,
                    )

        except Exception as erro:
            print(f"Erro: {erro}")
            return Response(
                {"error": "Erro ao processar a solicitação."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
