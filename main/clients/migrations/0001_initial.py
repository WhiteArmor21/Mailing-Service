# Generated by Django 4.0.3 on 2022-03-16 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=12, unique=True)),
                ('mobile_operator', models.CharField(max_length=3)),
                ('tag', models.CharField(blank=True, max_length=50)),
                ('client_time_zone', models.CharField(max_length=30)),
            ],
        ),
    ]