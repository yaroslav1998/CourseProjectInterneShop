# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-12 15:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024)),
                ('description', models.TextField()),
            ],
            options={
                'db_table': 'manufacturer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024)),
                ('meta_title', models.CharField(max_length=1024)),
                ('meta_h1', models.CharField(max_length=1024)),
                ('meta_description', models.TextField()),
                ('meta_keywords', models.CharField(max_length=1024)),
                ('description', models.TextField()),
                ('description_full', models.TextField()),
                ('link', models.CharField(max_length=1024)),
                ('enabled', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=65)),
                ('views', models.IntegerField()),
                ('article', models.CharField(max_length=1024)),
            ],
            options={
                'db_table': 'product',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('comment', models.TextField()),
                ('enabled', models.IntegerField()),
                ('comment_admin', models.TextField()),
            ],
            options={
                'db_table': 'product_review',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProductSale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_old', models.DecimalField(decimal_places=2, max_digits=65)),
                ('sale_coef', models.IntegerField()),
            ],
            options={
                'db_table': 'product_sale',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/products_image/')),
            ],
        ),
        migrations.CreateModel(
            name='ProductRate',
            fields=[
                ('id', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='product.Product')),
                ('rate', models.IntegerField()),
            ],
            options={
                'db_table': 'product_rate',
                'managed': False,
            },
        ),
        migrations.AddField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.Product'),
        ),
    ]