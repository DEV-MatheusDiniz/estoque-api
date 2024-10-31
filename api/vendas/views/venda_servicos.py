from rest_framework.views import APIView, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from ..models.venda_servicos import VendaServicoModel
from ..models.vendas import VendasModel
from api.servicos.models.servicos import ServicoModel

from ..serializers.venda_servicos import VendaServicosSerializer


class VendaServicosAPIView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, id_venda, id_venda_servico=None):
        """
        Sempre deve receber o id_venda.
        Caso receba o id_venda_servico, retornar apenas o serviço
        """
        try:
            if id_venda_servico and id_venda:
                result = VendaServicoModel.objects.filter(fk_servico=id_venda_servico, fk_venda=id_venda)
            elif id_venda:
                result = VendaServicoModel.objects.filter(fk_venda=id_venda)

            serializer = VendaServicosSerializer(result, many=True).data

            return Response(serializer)

        except Exception as erro:
            print(erro)
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, id_venda):
        """
        Salvar o serviço de uma venda.

        Exemplo de requisição:
        {
            "fk_servico": 1
        }
        """
        try:
            requisicao = request.data

            # fk_servico
            servico = ServicoModel.objects.get(id=requisicao["fk_servico"])
            requisicao["fk_servico"] = servico

            # nu_valor_unitario
            requisicao["nu_valor_unitario"] = servico.nu_valor_unitario

            # fk_venda
            venda = VendasModel.objects.get(id=id_venda)
            requisicao["fk_venda"] = venda

            # Verificar se já tem o serviço na venda
            venda_possui_servico = VendaServicoModel.objects.filter(fk_venda=venda, fk_servico=servico).first()

            if venda_possui_servico:
                """Soma mais 1 quantidade no serviço já existente"""
                venda_possui_servico.nu_quantidade += 1
                venda_possui_servico.save()

                venda_servico = venda_possui_servico
            else:
                """Cria um novo serviço para venda"""
                venda_servico = VendaServicoModel.objects.create(**requisicao)

            # Atualizar valor total da venda
            venda.nu_valor_total += venda_servico.nu_valor_unitario
            venda.save()

            serializer = VendaServicosSerializer(venda_servico).data

            return Response(serializer, status=status.HTTP_200_OK)

        except Exception as erro:
            print(erro)
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id_venda, id_venda_servico):
        """
        Altualiza o serviço de uma venda

        Deve ser passado apenas nu_quantidade na requisição
        """
        try:
            # Obter dados da venda
            venda = VendasModel.objects.get(id=id_venda)

            # Obter dados do serviço atual de uma venda
            venda_servico = VendaServicoModel.objects.get(
                fk_servico=id_venda_servico, fk_venda=id_venda
            )
            serializer_venda_servico_atual = VendaServicosSerializer(
                venda_servico
            ).data

            # Atualizar serviço
            nu_quantidade = request.data["nu_quantidade"]

            venda_servico.nu_quantidade = nu_quantidade
            venda_servico.save()

            # Atualizar venda
            diferenca_nu_subtotal = (
                venda_servico.nu_subtotal
                - serializer_venda_servico_atual["nu_subtotal"]
            )

            venda.nu_valor_total += diferenca_nu_subtotal
            venda.save()
            
            # Obter dados do serviço atualizado da venda
            venda_servico_atualizado = VendaServicoModel.objects.get(
                fk_servico=id_venda_servico, fk_venda=id_venda
            )
            serializer_venda_servico_atualizado = VendaServicosSerializer(
                venda_servico_atualizado
            ).data

            return Response(serializer_venda_servico_atualizado, status=status.HTTP_200_OK)

        except VendaServicoModel.DoesNotExist:
                return Response(
                    {"error": "Serviço não encontrado."},
                    status=status.HTTP_404_NOT_FOUND,
                )
        
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
