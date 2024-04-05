from django.contrib import admin
from meuestoque_replacement.replacements.models import PedidoReposicao


@admin.register(PedidoReposicao)
class ReposicaoAdmin(admin.ModelAdmin):
    model = PedidoReposicao

