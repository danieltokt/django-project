# Generated by Django 5.1.1 on 2024-10-23 17:43

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_manager', '0002_remove_event_location_event_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='title',
            new_name='location',
        ),
        migrations.AddField(
            model_name='event',
            name='name',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
