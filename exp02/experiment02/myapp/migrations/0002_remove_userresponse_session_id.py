# Generated by Django 4.2.7 on 2023-11-26 11:35

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userresponse",
            name="session_id",
        ),
    ]
