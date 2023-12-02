# Generated by Django 4.1 on 2023-12-02 11:58

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
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
                ("title", models.CharField(max_length=50)),
                ("slug", models.SlugField()),
                ("short_description", models.CharField(max_length=255)),
                ("image", models.ImageField(upload_to="images/")),
                ("blog_text", models.TextField()),
            ],
        ),
    ]
