# Generated by Django 4.2.17 on 2025-01-03 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Watchlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.EmailField(max_length=254)),
                ('video_id', models.CharField(max_length=255)),
                ('added_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
