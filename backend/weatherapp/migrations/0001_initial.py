# Generated by Django 2.2.16 on 2020-09-16 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Humidity",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("humidity", models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name="Locations",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name="Name",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("city", models.CharField(max_length=256)),
                ("state", models.CharField(max_length=2)),
                ("latitude", models.CharField(max_length=256)),
                ("longitude", models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name="Temperature",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("minimum", models.CharField(max_length=256)),
                ("maximum", models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name="Wind",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("wind_speed", models.CharField(max_length=256)),
            ],
        ),
    ]
