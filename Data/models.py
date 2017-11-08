# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Article(models.Model):
    name = models.CharField(max_length=1024)
    meta_title = models.CharField(max_length=1024)
    meta_h1 = models.CharField(max_length=1024)
    meta_description = models.TextField()
    meta_keywords = models.CharField(max_length=1024)
    description = models.TextField()
    content = models.TextField()
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'article'


class Category(models.Model):
    name = models.CharField(max_length=1024)
    meta_title = models.CharField(max_length=1024)
    meta_h1 = models.CharField(max_length=1024)
    meta_description = models.TextField()
    meta_keywords = models.CharField(max_length=1024)
    content = models.TextField()
    pid = models.ForeignKey('Product', models.DO_NOTHING, db_column='pid')
    img = models.CharField(max_length=1024)
    sort_order = models.IntegerField()
    link = models.CharField(max_length=1024)
    enabled = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'category'


class CategoryParameter(models.Model):
    name = models.CharField(max_length=1024)
    cid = models.ForeignKey(Category, models.DO_NOTHING, db_column='cid')

    class Meta:
        managed = False
        db_table = 'category_parameter'


class Manufacturer(models.Model):
    name = models.CharField(max_length=1024)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'manufacturer'


class Order(models.Model):
    uid = models.ForeignKey('User', models.DO_NOTHING, db_column='uid')
    adress = models.TextField()
    phone = models.CharField(max_length=1024)
    date = models.DateTimeField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'order'


class OrderItem(models.Model):
    oid = models.ForeignKey(Order, models.DO_NOTHING, db_column='oid')
    pid = models.ForeignKey('Product', models.DO_NOTHING, db_column='pid')
    count = models.DecimalField(max_digits=65, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'order_item'


class Product(models.Model):
    id = models.ForeignKey('ProductArticle', models.DO_NOTHING, db_column='id', primary_key=True)
    name = models.CharField(max_length=1024)
    meta_title = models.CharField(max_length=1024)
    meta_h1 = models.CharField(max_length=1024)
    meta_description = models.TextField()
    meta_keywords = models.CharField(max_length=1024)
    description = models.TextField()
    description_full = models.TextField()
    cid = models.ForeignKey(Category, models.DO_NOTHING, db_column='cid')
    link = models.CharField(max_length=1024)
    enabled = models.IntegerField()
    price = models.DecimalField(max_digits=65, decimal_places=2)
    views = models.IntegerField()
    article = models.CharField(max_length=1024)
    manufacturer = models.ForeignKey(Manufacturer, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product'


class ProductArticle(models.Model):
    pid = models.IntegerField()
    aid = models.ForeignKey(Article, models.DO_NOTHING, db_column='aid')

    class Meta:
        managed = False
        db_table = 'product_article'


class ProductParameterValue(models.Model):
    product = models.ForeignKey(Product, models.DO_NOTHING)
    parameter = models.ForeignKey(CategoryParameter, models.DO_NOTHING)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'product_parameter_value'


class ProductRate(models.Model):
    id = models.ForeignKey(Product, models.DO_NOTHING, db_column='id', primary_key=True)
    rate = models.IntegerField()
    uid = models.ForeignKey('User', models.DO_NOTHING, db_column='uid')

    class Meta:
        managed = False
        db_table = 'product_rate'


class ProductReview(models.Model):
    uid = models.ForeignKey('User', models.DO_NOTHING, db_column='uid')
    date = models.DateTimeField()
    comment = models.TextField()
    enabled = models.IntegerField()
    comment_admin = models.TextField()
    pid = models.ForeignKey(Product, models.DO_NOTHING, db_column='pid')

    class Meta:
        managed = False
        db_table = 'product_review'


class ProductSale(models.Model):
    pid = models.ForeignKey(Product, models.DO_NOTHING, db_column='pid')
    price_old = models.DecimalField(max_digits=65, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'product_sale'


class ProductStockBalance(models.Model):
    pid = models.ForeignKey(Product, models.DO_NOTHING, db_column='pid')
    sid = models.ForeignKey('Stock', models.DO_NOTHING, db_column='sid')
    balance = models.DecimalField(max_digits=65, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'product_stock_balance'


class Stock(models.Model):
    name = models.CharField(max_length=1024)
    adress = models.TextField()
    enabled = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stock'


class User(models.Model):
    email = models.CharField(max_length=1024)
    password = models.CharField(max_length=1024)
    role = models.CharField(max_length=1024)
    reg_date = models.DateTimeField()
    name = models.CharField(max_length=1024)
    phone = models.CharField(max_length=1024)
    adress = models.CharField(max_length=1024)

    class Meta:
        managed = False
        db_table = 'user'
