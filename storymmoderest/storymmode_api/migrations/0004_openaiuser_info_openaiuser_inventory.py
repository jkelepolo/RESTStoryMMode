# Generated by Django 4.2.11 on 2024-04-01 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("storymmode_api", "0003_openaiuser_character_tags_location_tags"),
    ]

    operations = [
        migrations.AddField(
            model_name="openaiuser",
            name="info",
            field=models.TextField(default=""),
        ),
        migrations.AddField(
            model_name="openaiuser",
            name="inventory",
            field=models.TextField(default=""),
        ),
    ]
