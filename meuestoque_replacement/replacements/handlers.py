from django_socio_grpc.services.app_handler_registry import AppHandlerRegistry
from meuestoque_replacement.replacements.services import ReplacementService


def grpc_handlers(server):
    app_registry = AppHandlerRegistry("replacements", server)
    app_registry.register(ReplacementService)
