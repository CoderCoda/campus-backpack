# Generated by Django 2.0.3 on 2018-04-22 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0006_auto_20180417_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='textbook',
            name='price',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='textbook',
            name='cover_Image_URL',
            field=models.URLField(null=True),
        ),
    ]
