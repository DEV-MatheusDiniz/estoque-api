# Generated by Django 5.1.2 on 2024-10-20 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0005_remove_vendaservicomodel_nu_subtotal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendaservicomodel',
            name='nu_quantidade',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
        ),
    ]