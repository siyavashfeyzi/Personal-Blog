# Generated by Django 4.1 on 2023-12-04 14:22

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("Blog", "0007_post_title index"),
    ]

    operations = [
        migrations.RenameIndex(
            model_name="post",
            new_name="title_index",
            old_name="title index",
        ),
    ]
