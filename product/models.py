from __future__ import unicode_literals

from django.db import models

class Manufacturer(models.Model):
    name = models.CharField(max_length=1024)
    description = models.TextField()
    class Meta:
        managed = False
        db_table = 'manufacturer'
    def __str__(self):
        return "%s" % self.name

class Product(models.Model):
    name = models.CharField(max_length=1024)
    meta_title = models.CharField(max_length=1024)
    meta_h1 = models.CharField(max_length=1024)
    meta_description = models.TextField()
    meta_keywords = models.CharField(max_length=1024)
    short_description = models.TextField()
    description = models.TextField()
    enabled = models.BooleanField()
    price = models.DecimalField(max_digits=65, decimal_places=2,default=0)
    manufacturer=models.ForeignKey(Manufacturer,models.DO_NOTHING,db_column='manufacturer')
    category=models.ForeignKey('category.Category',models.DO_NOTHING,db_column='cid')
    is_active=models.BooleanField(db_column='is_active')
    class Meta:
        managed = False
        db_table = 'product'
    def __str__(self):
        return "%s" % self.name

class ProductImage(models.Model):
    product=models.ForeignKey(Product,models.DO_NOTHING)
    image=models.ImageField(upload_to="media/products_image/")
    def __str__(self):
        return "%s" % self.image

class ProductRate(models.Model):
    rate = models.IntegerField()
    uid = models.ForeignKey('landing.User', models.DO_NOTHING, db_column='uid')
    pid = models.ForeignKey(Product,models.DO_NOTHING,db_column='pid')
    class Meta:
        managed = False
        db_table = 'product_rate'
    def __str__(self):
        return "%s %s" % (self.id.name,self.rate)


class ProductReview(models.Model):
    uid = models.ForeignKey('landing.User', models.DO_NOTHING, db_column='uid')
    date = models.DateTimeField(auto_now_add=True,auto_now=False)
    comment = models.TextField()
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

