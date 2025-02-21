# Generated by Django 5.1.1 on 2024-09-16 20:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deceased', '0003_note'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='is_approved',
            new_name='approved',
        ),
        migrations.RenameField(
            model_name='note',
            old_name='text',
            new_name='content',
        ),
        migrations.RemoveField(
            model_name='note',
            name='deceased',
        ),
        migrations.AddField(
            model_name='note',
            name='deceased_person',
            field=models.ForeignKey(default=12, on_delete=django.db.models.deletion.CASCADE, to='deceased.deceasedperson'),
        ),
    ]
