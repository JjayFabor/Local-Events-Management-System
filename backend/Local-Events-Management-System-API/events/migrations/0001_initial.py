# Generated by Django 5.0.7 on 2024-08-06 01:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='EventModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=100)),
                ('event_hosts', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('image_url', models.URLField()),
                ('event_date', models.DateTimeField()),
                ('location', models.CharField(max_length=100)),
                ('registration_deadline', models.DateTimeField()),
                ('capacity', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('UPCOMING', 'UPCOMING'), ('ONGOING', 'ONGOING'), ('COMPLETED', 'COMPLETED'), ('CANCELED', 'CANCELED')], default='UPCOMING', max_length=12)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.category')),
            ],
        ),
    ]
