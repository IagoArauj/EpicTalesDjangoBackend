# Generated by Django 5.1 on 2024-08-28 22:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("campaigns", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="campaign",
            name="invite_link",
            field=models.CharField(default="hV1R7Ms8Mo", max_length=10),
        ),
    ]
