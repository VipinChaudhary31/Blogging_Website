# Generated by Django 4.1 on 2022-08-24 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "Username",
                    models.CharField(max_length=100, primary_key=True, serialize=False),
                ),
                ("Name", models.CharField(max_length=100)),
                ("Email", models.CharField(max_length=100)),
                ("Password", models.CharField(max_length=100)),
            ],
            options={
                "db_table": "User",
            },
        ),
    ]
