from __future__ import unicode_literals

from django.db import models
class Order(models.Model):

    adress = models.TextField()
    phone = models.CharField(max_length=1024)
    date = models.DateTimeField(auto_now_add=True,auto_now=False)
    status = models.ForeignKey('Status',models.DO_NOTHING,db_column='status')
    uid = models.ForeignKey("landing.User", models.DO_NOTHING, db_column='uid')
    class Meta:
        managed = False
        db_table = 'order'
    def __str__(self):
        return "%s" % (self.id)

class OrderItem(models.Model):
    oid = models.ForeignKey(Order, models.DO_NOTHING, db_column='oid')
    pid = models.ForeignKey("product.Product", models.DO_NOTHING, db_column='pid')
    count = models.IntegerField(default=1)
    Full_price=models.IntegerField()
    class Meta:
        managed = False
        db_table = 'order_item'
    def __str__(self):
        return "%s %s" % (self.oid,self.pid.name)

class Status(models.Model):
    name=models.CharField(max_length=30)
    class Meta:
        managed = False
        db_table = 'Status'
    def __str__(self):
        return "%s" % self.name