# Generated by Django 5.0.7 on 2024-09-13 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('riverdata', '0017_alter_combinedpredictions_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='alpinemeadowsgauge',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='alpinemeadowsweatherprediction',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='silvertonweatherprediction',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='alpinemeadowsgauge',
            name='date',
        ),
        migrations.RemoveField(
            model_name='alpinemeadowsgauge',
            name='time',
        ),
        migrations.RemoveField(
            model_name='alpinemeadowsweatherprediction',
            name='date',
        ),
        migrations.RemoveField(
            model_name='alpinemeadowsweatherprediction',
            name='time',
        ),
        migrations.RemoveField(
            model_name='silvertonweatherprediction',
            name='date',
        ),
        migrations.RemoveField(
            model_name='silvertonweatherprediction',
            name='time',
        ),
    ]
