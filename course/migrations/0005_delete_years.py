# Generated by Django 4.1.4 on 2023-11-04 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_rename_year_years'),
    ]

    operations = [
        migrations.DeleteModel(
            name='years',
        ),
    ]
