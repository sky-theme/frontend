# Generated by Django 4.2.6 on 2023-12-21 01:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("data_analysis", "0035_commentmodel"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="commentmodel",
            name="userId",
        ),
        migrations.AddField(
            model_name="commentmodel",
            name="userName",
            field=models.CharField(default="", max_length=255),
        ),
    ]