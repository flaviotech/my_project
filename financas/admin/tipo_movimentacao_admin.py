#Shift + Alt + O para organizar as importações (vs code)

from django.contrib import admin

from ..models import TipoMovimentacao


@admin.register(TipoMovimentacao)
class TipoMovimentacaoAdmin(admin.ModelAdmin):
    list_display = [
        'nome',
    ]

    search_fields = [
        'nome',
    ]
