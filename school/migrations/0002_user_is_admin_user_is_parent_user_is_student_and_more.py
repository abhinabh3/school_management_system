# Generated by Django 5.1.3 on 2024-11-08 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("school", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="is_admin",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="user",
            name="is_parent",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="user",
            name="is_student",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="user",
            name="is_teacher",
            field=models.BooleanField(default=False),
        ),
    ]
