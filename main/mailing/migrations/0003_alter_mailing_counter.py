# Generated by Django 4.0.3 on 2022-03-22 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0002_mailing_counter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='counter',
            field=models.IntegerField(default=0),
        ),
    ]
