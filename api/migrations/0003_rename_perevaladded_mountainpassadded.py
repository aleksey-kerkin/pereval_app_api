# Generated by Django 5.0.6 on 2024-06-23 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_rename_coords_coord_rename_images_image_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="PerevalAdded",
            new_name="MountainPassAdded",
        ),
    ]
