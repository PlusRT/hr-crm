# Generated by Django 2.0.6 on 2018-07-09 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0015_remove_vacancy_experience'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='comments',
            field=models.TextField(null=True),
        ),
    ]
