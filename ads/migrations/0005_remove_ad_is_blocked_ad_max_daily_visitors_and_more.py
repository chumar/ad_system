# Generated by Django 4.2.6 on 2023-10-27 19:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ads", "0004_alter_ad_locations"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="ad",
            name="is_blocked",
        ),
        migrations.AddField(
            model_name="ad",
            name="max_daily_visitors",
            field=models.PositiveIntegerField(default=100),
        ),
        migrations.RemoveField(
            model_name="ad",
            name="locations",
        ),
        migrations.DeleteModel(
            name="Location",
        ),
        migrations.AddField(
            model_name="ad",
            name="locations",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Karachi", "Karachi"),
                    ("Lahore", "Lahore"),
                    ("Multan", "Multan"),
                ],
                default="Karachi",
                max_length=100,
            ),
        ),
    ]