# Generated by Django 2.0.6 on 2018-07-11 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0004_auto_20180710_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requirement',
            name='type',
            field=models.CharField(choices=[('REQUIRED', 'Обязательные'), ('OPTIONAL', 'Опциональные'), ('GENERAL', 'Общие')], default=0, max_length=100),
        ),
    ]
