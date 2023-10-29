# Generated by Django 4.2.6 on 2023-10-27 19:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ads", "0009_alter_ad_locations"),
    ]

    operations = [
        migrations.AlterField(
            model_name="location",
            name="name",
            field=models.CharField(
                choices=[
                    ("Karachi", "Karachi"),
                    ("Lahore", "Lahore"),
                    ("Multan", "Multan"),
                ],
                default="Karachi",
                max_length=100,
                unique=True,
            ),
        ),
    ]