#Shift + Alt + O para organizar as importações (vs code)

from django.db import models


class TipoMovimentacao(models.Model):
    '''
    Classe para registrar os tipos de movimentação,
    além de desempenhar todas as funcionalidades relacionadas a um tipo de movimentação.
    '''

    nome = models.CharField(
        verbose_name='Nome',
        max_length=100
    )

    data_criacao = models.DateTimeField(
        verbose_name='Data de criação',
        auto_now_add=True
    )

    data_atualizacao = models.DateTimeField(
        verbose_name='Data de atualização',
        auto_now=True
    )

    def __str__(self):
        return self.nome
    
    class Meta:
        app_label = 'financas'
        verbose_name = 'Tipo de movimentação'
        verbose_name_plural = 'Tipos de movimentações'
