# Generated by Django 5.1.1 on 2024-09-21 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0002_timeline_deceased_timeline_year_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeline',
            name='event_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
