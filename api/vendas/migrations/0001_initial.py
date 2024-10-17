# Generated by Django 5.1.2 on 2024-10-17 00:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0001_initial'),
        ('produtos', '0002_alter_produtomodel_nu_quantidade_estoque'),
        ('servicos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='VendasModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_venda', models.DateTimeField()),
                ('nu_valor_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('dt_cadastro', models.DateTimeField(auto_now_add=True)),
                ('dt_alteracao', models.DateTimeField(auto_now=True, null=True)),
                ('fk_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.clientemodel')),
                ('fk_funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'vendas',
            },
        ),
        migrations.CreateModel(
            name='VendaServicoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nu_quantidade', models.DecimalField(decimal_places=2, max_digits=10)),
                ('nu_valor_unitario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('nu_subtotal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('dt_cadastro', models.DateTimeField(auto_now_add=True)),
                ('dt_alteracao', models.DateTimeField(auto_now=True, null=True)),
                ('fk_servico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicos.servicomodel')),
                ('fk_venda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendas.vendasmodel')),
            ],
            options={
                'db_table': 'venda_servicos',
            },
        ),
        migrations.CreateModel(
            name='VendaProdutoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nu_quantidade', models.DecimalField(decimal_places=2, max_digits=10)),
                ('nu_valor_unitario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('nu_subtotal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('dt_cadastro', models.DateTimeField(auto_now_add=True)),
                ('dt_alteracao', models.DateTimeField(auto_now=True, null=True)),
                ('fk_produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.produtomodel')),
                ('fk_venda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendas.vendasmodel')),
            ],
            options={
                'db_table': 'venda_produtos',
            },
        ),
    ]
