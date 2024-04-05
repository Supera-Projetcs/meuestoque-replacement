from django_socio_grpc import generics
from meuestoque_replacement.replacements.models import PedidoReposicao
from meuestoque_replacement.replacements.serializers import ReplacementProtoSerializer


class ReplacementService(generics.AsyncModelService):
    queryset = PedidoReposicao.objects.all()
    serializer_class = ReplacementProtoSerializer


