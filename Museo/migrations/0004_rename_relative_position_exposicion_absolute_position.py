# Generated by Django 5.0.6 on 2024-10-05 18:29

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("Museo", "0003_remove_exposicion_museo_exposicion_relative_position_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="exposicion",
            old_name="relative_position",
            new_name="absolute_position",
        ),
    ]
