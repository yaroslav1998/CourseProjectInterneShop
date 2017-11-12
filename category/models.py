from __future__ import unicode_literals

from django.db import models
class Category(models.Model):
    name = models.CharField(max_length=1024)
    meta_title = models.CharField(max_length=1024)
    meta_h1 = models.CharField(max_length=1024)
    meta_description = models.TextField()
    meta_keywords = models.CharField(max_length=1024)
    content = models.TextField()
    pid = models.ForeignKey('product.Product', models.DO_NOTHING, db_column='pid')
    class Meta:
        managed = False
        db_table = 'category'
    def __str__(self):
        return "%s" % self.name