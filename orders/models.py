from __future__ import unicode_literals

from django.db import models
class Order(models.Model):
    uid = models.ForeignKey("landing.User", models.DO_NOTHING, db_column='uid')
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
    pid = models.ForeignKey("product.Product", models.DO_NOTHING, db_column='pid')
    count = models.DecimalField(max_digits=65, decimal_places=2)
    class Meta:
        managed = False
        db_table = 'order_item'
    def __str__(self):
        return "%s %s" % (self.oid,self.pid.name)