#Shift + Alt + O para organizar as importações (vs code)

from django.contrib import admin

from ..models import Movimentacao


@admin.register(Movimentacao)
class MovimentacaoAdmin(admin.ModelAdmin):
    list_display = [
        'nome',
        'valor',
        'data',
    ]

    search_fields = [
        'nome',
        'valor',
        'data',
    ]

    list_filter = [
        'data',
    ]
