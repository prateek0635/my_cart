# Generated by Django 3.0.2 on 2020-04-15 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='shop_id',
            field=models.CharField(default='', max_length=20),
        ),
    ]
