# Generated by Django 2.0.3 on 2018-04-22 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0007_auto_20180422_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textbook',
            name='cover_Image_URL',
            field=models.URLField(max_length=400, null=True),
        ),
    ]