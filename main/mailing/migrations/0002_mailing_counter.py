# Generated by Django 4.0.3 on 2022-03-22 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailing',
            name='counter',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]