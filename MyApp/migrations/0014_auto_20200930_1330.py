# Generated by Django 3.0.2 on 2020-09-30 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0013_auto_20200930_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='slug',
            field=models.SlugField(blank=True, max_length=2000, unique=True),
        ),
    ]
