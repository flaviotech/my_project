# Generated by Django 4.0.2 on 2022-02-08 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movimentacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('descricao', models.TextField(blank=True, null=True, verbose_name='Descrição')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor')),
                ('data', models.DateField(verbose_name='Data')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
                ('data_atualizacao', models.DateTimeField(auto_now=True, verbose_name='Data de atualização')),
            ],
            options={
                'verbose_name': 'Movimentação',
                'verbose_name_plural': 'Movimentações',
            },
        ),
    ]
