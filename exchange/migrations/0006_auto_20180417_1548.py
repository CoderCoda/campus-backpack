# Generated by Django 2.0.3 on 2018-04-17 19:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0005_auto_20180417_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textbook',
            name='ISBN',
            field=models.CharField(max_length=13, null=True, validators=[django.core.validators.RegexValidator('\\d{13}', 'ISBN must be 13 digits')]),
        ),
    ]
