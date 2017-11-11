# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from datetime import datetime



class Category(models.Model):
    name = models.CharField(max_length=1024)
    meta_title = models.CharField(max_length=1024)
    meta_h1 = models.CharField(max_length=1024)
    meta_description = models.TextField()
    meta_keywords = models.CharField(max_length=1024)
    content = models.TextField()
    pid = models.ForeignKey('Product', models.DO_NOTHING, db_column='pid')
    class Meta:
        managed = False
        db_table = 'category'
    def __str__(self):
        return "%s" % self.name

class Manufacturer(models.Model):
    name = models.CharField(max_length=1024)
    description = models.TextField()
    class Meta:
        managed = False
        db_table = 'manufacturer'
    def __str__(self):
        return "%s" % self.name


class Order(models.Model):
    uid = models.ForeignKey('User', models.DO_NOTHING, db_column='uid')
    adress = models.TextField()
    phone = models.CharField(max_length=1024)
    date = models.DateTimeField(auto_now_add=True,auto_now=False)
    status = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'order'
    def __str__(self):
        return "%s %s" % (self.uid.name,self.id)


class OrderItem(models.Model):
    oid = models.ForeignKey(Order, models.DO_NOTHING, db_column='oid')
    pid = models.ForeignKey('Product', models.DO_NOTHING, db_column='pid')
    count = models.DecimalField(max_digits=65, decimal_places=2)
    class Meta:
        managed = False
        db_table = 'order_item'
    def __str__(self):
        return "%s %s" % (self.oid,self.pid.name)

class Product(models.Model):
    name = models.CharField(max_length=1024)
    meta_title = models.CharField(max_length=1024)
    meta_h1 = models.CharField(max_length=1024)
    meta_description = models.TextField()
    meta_keywords = models.CharField(max_length=1024)
    description = models.TextField()
    description_full = models.TextField()
    link = models.CharField(max_length=1024)
    enabled = models.IntegerField()
    price = models.DecimalField(max_digits=65, decimal_places=2)
    views = models.IntegerField()
    article = models.CharField(max_length=1024)
    manufacturer = models.ForeignKey(Manufacturer, models.DO_NOTHING)
    class Meta:
        managed = False
        db_table = 'product'
    def __str__(self):
        return "%s %s" % (self.id,self.name)

class ProductImage(models.Model):
    product=models.ForeignKey(Product,models.DO_NOTHING)
    image=models.ImageField(upload_to="media/products_image/")

class ProductRate(models.Model):
    id = models.ForeignKey(Product, models.DO_NOTHING, db_column='id', primary_key=True)
    rate = models.IntegerField()
    uid = models.ForeignKey('User', models.DO_NOTHING, db_column='uid')
    class Meta:
        managed = False
        db_table = 'product_rate'
    def __str__(self):
        return "%s %s" % (self.id.name,self.rate)


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
    def __str__(self):
        return "%s %s" % (self.uid.name,self.comment)

class ProductSale(models.Model):
    pid = models.ForeignKey(Product, models.DO_NOTHING, db_column='pid')
    price_old = models.DecimalField(max_digits=65, decimal_places=2)
    sale_coef=models.IntegerField()
    class Meta:
        managed = False
        db_table = 'product_sale'
    def __str__(self):
        return "%s %s" % (self.pid.name,self.sale_coef)

class ProductStockBalance(models.Model):
    pid = models.ForeignKey(Product, models.DO_NOTHING, db_column='pid')
    sid = models.ForeignKey('Stock', models.DO_NOTHING, db_column='sid')
    balance = models.DecimalField(max_digits=65, decimal_places=2)
    class Meta:
        managed = False
        db_table = 'product_stock_balance'
    def __str__(self):
        return "%s %s" % (self.pid.name,self.sale_coef)

class Stock(models.Model):
    name = models.CharField(max_length=1024)
    adress = models.TextField()
    enabled = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'stock'
    def __str__(self):
        return "%s %s" % (self.name,self.enabled)
class User(models.Model):
    email = models.EmailField(max_length=1024)
    password = models.CharField(max_length=1024)
    role = models.CharField(max_length=1024)
    reg_date = models.DateTimeField()
    name = models.CharField(max_length=1024)
    phone = models.CharField(max_length=1024)
    adress = models.CharField(max_length=1024)
    class Meta:
        managed = False
        db_table = 'user'
    def __str__(self):
        return "%s %s" % (self.name,self.adress)