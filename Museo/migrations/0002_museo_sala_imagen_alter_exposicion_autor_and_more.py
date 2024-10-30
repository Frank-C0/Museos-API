# Generated by Django 5.0.6 on 2024-10-05 17:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Museo", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Museo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=100)),
                ("descripcion", models.TextField()),
                ("imagen", models.URLField(blank=True, null=True)),
                ("width", models.FloatField()),
                ("height", models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name="sala",
            name="imagen",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="exposicion",
            name="autor",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="Museo.autor",
            ),
        ),
        migrations.AlterField(
            model_name="exposicion",
            name="sala",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="Museo.sala",
            ),
        ),
        migrations.AddField(
            model_name="exposicion",
            name="museo",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="Museo.museo",
            ),
        ),
        migrations.AddField(
            model_name="sala",
            name="museo",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="Museo.museo",
            ),
            preserve_default=False,
        ),
    ]
