# Generated by Django 3.0.2 on 2020-09-30 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0012_shop_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='affiliate',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='products',
            name='affiliate_img',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='products',
            name='affiliate_link',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='products',
            name='review',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='products',
            name='slug',
            field=models.SlugField(blank=True, max_length=2000),
        ),
        migrations.AddField(
            model_name='shop',
            name='bottomhtml',
            field=models.CharField(blank=True, default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='shop',
            name='tophtml',
            field=models.CharField(blank=True, default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='products',
            name='prod_disc',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='products',
            name='prod_name',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='shop',
            name='category',
            field=models.CharField(choices=[('Grocery', 'Grocery'), ('Medical', 'Medical'), ('DailyE', 'DailyE'), ('Mobile', 'Mobile'), ('electronics', 'electronics'), ('clothing', 'clothing'), ('food', 'food'), ('furtunier', 'furtunier'), ('gifts', 'gifts'), ('computers', 'computers'), ('jewellery', 'jewellery'), ('book', 'book'), ('Stationery', 'Stationery')], default='Grocery', max_length=20),
        ),
        migrations.AlterField(
            model_name='shop',
            name='shop_add',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='shop',
            name='shop_disc',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='shop',
            name='shop_name',
            field=models.CharField(max_length=500),
        ),
    ]