# Generated by Django 4.2.11 on 2024-04-03 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("storymmode_api", "0004_openaiuser_info_openaiuser_inventory"),
    ]

    operations = [
        migrations.CreateModel(
            name="Item",
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
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("meta_description", models.TextField()),
                ("tags", models.TextField(default="")),
            ],
        ),
    ]