# Generated by Django 5.1.2 on 2024-10-16 03:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0001_initial'),
        ('servicos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VendasModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_venda', models.DateTimeField()),
                ('nu_valor_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('dt_cadastro', models.DateTimeField(auto_now_add=True)),
                ('dt_alteracao', models.DateTimeField(auto_now=True, null=True)),
                ('fk_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.clientemodel')),
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
    ]
