# Generated by Django 4.1 on 2023-12-04 13:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Blog", "0005_alter_post_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="title",
            field=models.CharField(max_length=255),
        ),
    ]