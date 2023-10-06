# Generated by Django 4.1.4 on 2023-10-06 17:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0003_board_ten_board_twelve_university'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fathers_name', models.CharField(blank=True, max_length=255)),
                ('mothers_name', models.CharField(blank=True, max_length=255)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=255)),
                ('address', models.TextField(blank=True)),
                ('user_img', models.FileField(blank=True, upload_to='')),
                ('percentage_ten', models.CharField(blank=True, max_length=255)),
                ('ten_result', models.FileField(blank=True, upload_to='')),
                ('percentage_twelve', models.CharField(blank=True, max_length=255)),
                ('twelve_result', models.FileField(blank=True, upload_to='')),
                ('cgpa', models.CharField(blank=True, max_length=255)),
                ('s_start', models.CharField(blank=True, max_length=255)),
                ('s_end', models.CharField(blank=True, max_length=255)),
                ('status', models.CharField(max_length=255)),
                ('board_ten', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='course.board_ten')),
                ('board_twelve', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='course.board_twelve')),
                ('course', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='course.courses')),
                ('university', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='course.university')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
