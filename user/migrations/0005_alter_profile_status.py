# Generated by Django 4.1.4 on 2023-10-06 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_profile_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='status',
            field=models.CharField(blank=True, choices=[('pending', 'pending'), ('accept', 'accept')], max_length=255),
        ),
    ]
