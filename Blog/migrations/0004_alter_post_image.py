# Generated by Django 4.1 on 2023-12-03 10:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Blog", "0003_alter_post_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="image/"),
        ),
    ]