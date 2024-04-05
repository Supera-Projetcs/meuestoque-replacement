from django_socio_grpc import proto_serializers
from rest_framework import serializers
from meuestoque_replacement.replacements.models import PedidoReposicao
from meuestoque_replacement.replacements.grpc.replacements_pb2 import (
    ReplacementResponse,
    ReplacementListResponse,
)


class ReplacementProtoSerializer(proto_serializers.ModelProtoSerializer):

    class Meta:
        model = PedidoReposicao
        fields = "__all__"
        proto_class = ReplacementResponse
        proto_class_list = ReplacementListResponse
