# Generated by Django 5.0.7 on 2024-08-06 01:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='eventmodel',
            options={'permissions': [('view_event', 'Can view event'), ('change_event', 'Can change event'), ('delete_event', 'Can delete event'), ('add_event', 'Can add event')]},
        ),
    ]
