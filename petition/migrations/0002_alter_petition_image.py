# Generated by Django 4.1.3 on 2022-11-06 15:19

from django.db import migrations, models
import petition.models


class Migration(migrations.Migration):

    dependencies = [
        ("petition", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="petition",
            name="image",
            field=models.ImageField(
                default="default.jpg", upload_to=petition.models.user_directory_path
            ),
        ),
    ]
