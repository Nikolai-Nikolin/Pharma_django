# Generated by Django 5.0.2 on 2024-02-11 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharma', '0002_remove_cure_book_location_cure_cure_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='cure',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
