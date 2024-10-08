# Generated by Django 5.0.7 on 2024-09-11 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riverdata', '0008_granitefallsforecast_prediction_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='alpinemeadowsgauge',
            name='datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='alpinemeadowsweatherprediction',
            name='datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='combinedgauges',
            name='datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='combinedpredictions',
            name='datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='granitefallsforecast',
            name='datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='granitefallsgauge',
            name='datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='granitefallsprediction',
            name='datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='jordanroadgauge',
            name='datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='silvertonweatherprediction',
            name='datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
