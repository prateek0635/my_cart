# Generated by Django 3.0.2 on 2020-10-04 05:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MyApp', '0017_auto_20201002_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='MRP',
            field=models.FloatField(blank=True, default=20000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='products',
            name='discount',
            field=models.FloatField(blank=True, default=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='products',
            name='rating',
            field=models.FloatField(default=5),
        ),
        migrations.AddField(
            model_name='shop',
            name='live',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='rateprod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('review', models.TextField(blank=True)),
                ('prod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.products')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
