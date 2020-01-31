from django.db import models
from django.contrib import admin
from django.utils import timezone
from django.conf import settings
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
    date = models.DateTimeField(auto_now_add=True, blank=True)
    



admin.site.register(LinkTable)