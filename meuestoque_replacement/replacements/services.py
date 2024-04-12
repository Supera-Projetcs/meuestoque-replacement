from django_socio_grpc import generics
from meuestoque_replacement.replacements.models import PedidoReposicao
from meuestoque_replacement.replacements.serializers import ReplacementProtoSerializer
from django_socio_grpc.decorators import grpc_action
from meuestoque_replacement.replacements.grpc.replacements_pb2 import Dashmost_replacedResponse
from django.db.models import Max, Sum
from asgiref.sync import sync_to_async


class ReplacementService(generics.AsyncModelService):
    queryset = PedidoReposicao.objects.all()
    serializer_class = ReplacementProtoSerializer

    async def PartialUpdate(self, request, context):
        instance = await self.aget_object()
        serializer = self.get_serializer(instance, message=request)
        serializer.is_valid(raise_exception=True)
        await self.aperform_partial_update(serializer)

        if getattr(instance, "_prefetched_objects_cache", None):
            instance._prefetched_objects_cache = {}

        return serializer.message


class DashService(generics.GenericService):

    @grpc_action(
        response=[
            {
                "name": "produto",
                "type": "int32",
            },
            {
                "name": "quantidade",
                "type": "int32",
            },
        ],
    )
    async def most_replaced(self, request, context):

        dash_sync = PedidoReposicao.objects.values("produto").annotate(quantity=Sum("quantidade")).order_by("-quantidade")
        dash = await sync_to_async(list)(dash_sync)

        response = Dashmost_replacedResponse(produto=dash[0]['produto'], quantidade=dash[0]['quantity'])

        return response
