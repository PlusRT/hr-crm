# Generated by Django 2.0.6 on 2018-06-30 09:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('departments', '0002_auto_20180628_1703'),
        ('vacancies', '0006_auto_20180630_0807'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='requierements',
            field=models.ManyToManyField(related_name='vacancies', to='departments.Requirement'),
        ),
    ]
