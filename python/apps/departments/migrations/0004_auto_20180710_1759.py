# Generated by Django 2.0.6 on 2018-07-10 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0003_auto_20180710_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requirement',
            name='type',
            field=models.CharField(choices=[('REQUIRED', 'ОБЯЗАТЕЛЬНЫЕ'), ('OPTIONAL', 'ОПЦИОНАЛЬНЫЕ'), ('GENERAL', 'ОБЩИЕ')], default=0, max_length=100),
        ),
    ]