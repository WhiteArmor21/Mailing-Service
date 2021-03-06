# Generated by Django 4.0.3 on 2022-03-18 19:04

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('message', models.TextField(max_length=500)),
                ('mobile_operator', models.CharField(blank=True, max_length=3)),
                ('tag', models.CharField(blank=True, max_length=50)),
                ('completion_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(max_length=50)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.client')),
                ('mailing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='mailing.mailing')),
            ],
        ),
    ]
