# Generated by Django 4.2.6 on 2023-10-27 18:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ads", "0003_alter_ad_locations"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ad",
            name="locations",
            field=models.ManyToManyField(
                choices=[
                    ("Karachi", "Karachi"),
                    ("Lahore", "Lahore"),
                    ("Multan", "Multan"),
                ],
                to="ads.location",
            ),
        ),
    ]
