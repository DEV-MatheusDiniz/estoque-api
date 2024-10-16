# Generated by Django 5.1.2 on 2024-10-16 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClienteModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ds_nome', models.CharField(max_length=100)),
                ('nu_telefone', models.IntegerField(max_length=11)),
                ('ds_email', models.CharField(max_length=100)),
                ('ds_endereco', models.TextField()),
                ('dt_cadastro', models.DateTimeField(auto_now_add=True)),
                ('dt_alteracao', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'clientes',
            },
        ),
    ]