# Generated by Django 3.2.18 on 2023-04-26 23:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library_database', '0006_asset_review'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Asset',
            new_name='AssetType',
        ),
    ]