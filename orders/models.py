from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import post_save

class Order(models.Model):

    adress = models.TextField()
    phone = models.CharField(max_length=1024)
    date = models.DateTimeField(auto_now_add=True,auto_now=False)
    status = models.ForeignKey('Status',models.DO_NOTHING,db_column='status')
    uid = models.ForeignKey("landing.User", models.DO_NOTHING, db_column='uid')
    full_price=models.DecimalField(max_digits=65,decimal_places=2,default=0)
    is_active=models.BooleanField()
    class Meta:
        managed = False
        db_table = 'order'
    def __str__(self):
        return "%s" % (self.id)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, models.DO_NOTHING, db_column='oid')
    pid = models.ForeignKey("product.Product", models.DO_NOTHING, db_column='pid')
    price_per_item=models.DecimalField(max_digits=65,decimal_places=2,default=0)
    count = models.IntegerField(default=1)
    Full_price=models.DecimalField(max_digits=65,decimal_places=2,default=0)
    is_active=models.BooleanField()
    class Meta:
        managed = False
        db_table = 'order_item'

    def __str__(self):
        return "%s %s" % (self.order,self.pid.name)

    def save(self,*args,**kwargs):
        self.price_per_item=self.pid.price
        self.Full_price = self.count*self.price_per_item
        super(OrderItem, self).save(*args, **kwargs)

def orderitem_post_save(sender, instance, created, **kwargs):
    order = instance.order
    products_in_order = OrderItem.objects.filter(order=order, is_active=True)
    order_full_price = 0
    for item in products_in_order:
        order_full_price = order_full_price + item.Full_price
    instance.order.full_price = order_full_price
    instance.order.save(force_update=True)

post_save.connect(orderitem_post_save, sender=OrderItem)


class Status(models.Model):
    name=models.CharField(max_length=30)
    class Meta:
        managed = False
        db_table = 'Status'
    def __str__(self):
        return "%s" % self.name