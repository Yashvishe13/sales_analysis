# Generated by Django 4.0.3 on 2022-03-11 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_sales_webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='transactions',
            name='product',
        ),
        migrations.AddField(
            model_name='transactions',
            name='product',
            field=models.ManyToManyField(to='shop_sales_webapp.product'),
        ),
    ]