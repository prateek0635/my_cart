# Generated by Django 3.0.2 on 2020-05-08 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0010_auto_20200508_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rateing',
            name='review',
            field=models.TextField(blank=True),
        ),
    ]
