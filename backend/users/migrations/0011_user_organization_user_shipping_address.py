# Generated by Django 5.1.1 on 2024-09-20 16:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0003_remove_partner_name_partner_user_partner_username'),
        ('users', '0010_remove_user_organization_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='organizations.organization'),
        ),
        migrations.AddField(
            model_name='user',
            name='shipping_address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
