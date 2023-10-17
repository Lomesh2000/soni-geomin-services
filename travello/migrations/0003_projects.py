# Generated by Django 4.2.5 on 2023-10-16 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("travello", "0002_destination_price"),
    ]

    operations = [
        migrations.CreateModel(
            name="Projects",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("company_name", models.CharField(max_length=100)),
                ("img", models.ImageField(upload_to="projects_pics")),
                ("desc", models.TextField()),
                ("equipments_used", models.TextField()),
            ],
        ),
    ]
