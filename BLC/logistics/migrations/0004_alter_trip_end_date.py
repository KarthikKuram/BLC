# Generated by Django 4.0.5 on 2022-09-23 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistics', '0003_rename_date_trip_start_date_trip_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
