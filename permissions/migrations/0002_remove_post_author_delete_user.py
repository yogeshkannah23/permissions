# Generated by Django 5.1 on 2024-08-26 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("permissions", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="author",
        ),
    ]
