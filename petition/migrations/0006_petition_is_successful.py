# Generated by Django 4.1.3 on 2022-11-20 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("petition", "0005_petition_recipient"),
    ]

    operations = [
        migrations.AddField(
            model_name="petition",
            name="is_successful",
            field=models.BooleanField(default=False),
        ),
    ]
