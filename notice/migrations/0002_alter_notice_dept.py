# Generated by Django 4.2.7 on 2023-11-10 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='dept',
            field=models.TextField(max_length=255),
        ),
    ]
