# Generated by Django 3.2.18 on 2023-04-26 23:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library_database', '0010_review_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='book_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='reviews', to='library_database.book'),
        ),
        migrations.AlterField(
            model_name='review',
            name='dvd_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='reviews', to='library_database.dvd'),
        ),
        migrations.AlterField(
            model_name='review',
            name='magazine_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='reviews', to='library_database.magazine'),
        ),
    ]
