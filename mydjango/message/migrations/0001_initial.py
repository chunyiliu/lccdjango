# Generated by Django 4.1.3 on 2022-11-15 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Message",
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
                ("name", models.CharField(max_length=50)),
                ("email", models.CharField(max_length=50)),
                ("subject", models.CharField(max_length=50)),
                ("content", models.TextField()),
                ("create_date", models.DateTimeField(auto_now_add=True)),
            ],
            options={"db_table": "contact",},
        ),
    ]
