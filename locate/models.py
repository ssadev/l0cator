from django.db import models
from django.contrib import admin
from django.utils import timezone
from django.conf import settings
from datetime import datetime
# Create your models here.

class LinkTable(models.Model):
    id = models.AutoField(primary_key=True)
    link = models.CharField(max_length=100)
    link_id = models.CharField(max_length=100)

    def __unicode__(self):
        return self.link_id

class Recordes(models.Model):
    id = models.AutoField(primary_key=True)
    link_id = models.CharField(max_length=100)
    date = models.DateTimeField(default=datetime.now, blank=True)
    recorde = models.TextField() 

    def __unicode__(self):
        return self.link_id


admin.site.register(LinkTable)
admin.site.register(Recordes)