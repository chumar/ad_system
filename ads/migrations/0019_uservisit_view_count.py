# Generated by Django 4.2.6 on 2023-10-29 08:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ads", "0018_filestored_file"),
    ]

    operations = [
        migrations.AddField(
            model_name="uservisit",
            name="view_count",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
