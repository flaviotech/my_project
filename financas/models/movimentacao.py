#Shift + Alt + O para organizar as importações (vs code)

from django.db import models


class Movimentacao(models.Model):
    '''
    Classe para registrar as movimentaçções, como gastos,
    reecitas e transferências, além de desempenhar
    todas as funcionalidades relacionadas a uma movimentação.
    '''

    nome = models.CharField(
        verbose_name='Nome',
        max_length=100
    )

    descricao = models.TextField(
        verbose_name='Descrição',
        blank=True, null=True
    )

    valor = models.DecimalField(
        verbose_name='Valor',
        max_digits=10, decimal_places=2
    )

    data = models.DateField(
        verbose_name='Data',
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
        verbose_name = 'Movimentação'
        verbose_name_plural = 'Movimentações'
