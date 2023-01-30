# Generated by Django 4.1.2 on 2022-11-07 11:52

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bankapp', '0006_alter_expenses_time_expenses_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expenses',
            name='good',
        ),
        migrations.RemoveField(
            model_name='savings',
            name='good',
        ),
        migrations.AddField(
            model_name='expenses',
            name='good_expenses',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='bankapp.goods'),
        ),
        migrations.AddField(
            model_name='savings',
            name='good_savings',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='bankapp.goods'),
        ),
        migrations.AlterField(
            model_name='expenses',
            name='time_expenses',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 7, 14, 52, 20, 970413)),
        ),
        migrations.AlterField(
            model_name='expenses',
            name='user_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='savings',
            name='time_saving',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 7, 14, 52, 20, 970413)),
        ),
        migrations.AlterField(
            model_name='savings',
            name='user_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]