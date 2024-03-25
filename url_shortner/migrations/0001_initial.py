# Generated by Django 5.0.3 on 2024-03-24 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_url', models.URLField(unique=True)),
                ('hashed_url', models.CharField(max_length=100, unique=True)),
                ('clicks', models.IntegerField(default=0)),
            ],
        ),
    ]
