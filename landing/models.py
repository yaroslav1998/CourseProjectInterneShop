from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    email = models.EmailField(max_length=1024)
    password = models.CharField(max_length=1024)
    role = models.CharField(max_length=1024)
    reg_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    name = models.CharField(max_length=1024)
    phone = models.CharField(max_length=1024)
    adress = models.CharField(max_length=1024)
    class Meta:
        managed = False
        db_table = 'user'
    def __str__(self):
        return "%s %s" % (self.name,self.adress)
