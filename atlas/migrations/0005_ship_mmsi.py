# Generated by Django 2.1.1 on 2018-11-13 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atlas', '0004_auto_20181112_0334'),
    ]

    operations = [
        migrations.AddField(
            model_name='ship',
            name='mmsi',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='MMSI'),
        ),
    ]
