# Generated by Django 2.0.3 on 2018-04-27 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0008_auto_20180422_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='code',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]