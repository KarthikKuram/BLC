# Generated by Django 4.0.5 on 2022-09-30 19:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistics', '0008_alter_wheel_purchase_date_alter_wheel_running_life_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wheel',
            name='purchase_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='wheel',
            name='running_life',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='wheel',
            name='serial_number',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]
