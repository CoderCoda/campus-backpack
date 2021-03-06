# Generated by Django 2.0.3 on 2018-04-06 16:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0002_textbook_seller'),
    ]

    operations = [
        migrations.AddField(
            model_name='textbook',
            name='condition',
            field=models.CharField(choices=[('N', 'New'), ('LN', 'Like New'), ('VG', 'Very Good'), ('G', 'Good'), ('A', 'Acceptable')], default='LN', max_length=2),
        ),
        migrations.AddField(
            model_name='textbook',
            name='isbn',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(9999999999999)]),
        ),
        migrations.AddField(
            model_name='textbook',
            name='notes',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
