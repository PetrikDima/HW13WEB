# Generated by Django 4.1.5 on 2023-01-30 18:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0012_rename_good_expenses_expenses_good_expense_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='time_expenses',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 30, 21, 40, 36, 298695)),
        ),
        migrations.AlterField(
            model_name='savings',
            name='time_saving',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 30, 21, 40, 36, 298695)),
        ),
    ]
