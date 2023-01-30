# Generated by Django 4.1.2 on 2022-10-14 08:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0002_rename_goods_goods_goods_expenses_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='time_expenses',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 14, 11, 23, 56, 464424)),
        ),
        migrations.AlterField(
            model_name='goods',
            name='goods_expenses',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='goods',
            name='goods_savings',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='savings',
            name='time_saving',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 14, 11, 23, 56, 463425)),
        ),
    ]
