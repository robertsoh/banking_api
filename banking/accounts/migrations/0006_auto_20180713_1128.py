# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-13 11:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20180713_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ormbankaccount',
            name='type',
            field=models.CharField(choices=[('SAVINGS_ACCOUNT', 'Cuenta de ahorros'), ('CURRENT_ACCOUNT', 'Cuenta corriente'), ('SALARY_ACCOUNT', 'Cuenta sueldo')], default='SAVINGS_ACCOUNT', max_length=15, null=True),
        ),
    ]
