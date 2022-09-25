# Generated by Django 4.0.5 on 2022-09-23 07:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='message_id',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
