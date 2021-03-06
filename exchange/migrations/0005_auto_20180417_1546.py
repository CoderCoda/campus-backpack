# Generated by Django 2.0.3 on 2018-04-17 19:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0004_auto_20180406_1246'),
    ]

    operations = [
        migrations.RenameField(
            model_name='textbook',
            old_name='cover_image_URL',
            new_name='cover_Image_URL',
        ),
        migrations.AddField(
            model_name='textbook',
            name='ISBN',
            field=models.IntegerField(max_length=13, null=True, validators=[django.core.validators.RegexValidator('\\d{11}', 'ISBN must be 13 digits')]),
        ),
    ]
