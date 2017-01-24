from __future__ import unicode_literals

from django.db import models
from django.utils.safestring import mark_safe
from django import forms

# Create your models here.


class oraclelist(models.Model):
    ipaddress=models.GenericIPAddressField(primary_key=True)
    #id=models.IntegerField(default=1)
    #ipaddress=models.GenericIPAddressField()
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    port=models.CharField(max_length=50)
    tnsname=models.CharField(max_length=100)
    version=models.CharField(max_length=100)
    charset=models.CharField(max_length=100)
    ncharset=models.CharField(max_length=100)
    hostname=models.CharField(max_length=100)
    alertpath=models.CharField(max_length=300)
    content=models.CharField(max_length=300)
    monitor_type=models.IntegerField(default=1)
    performance_type=models.IntegerField(default=0)
    hit_type=models.IntegerField(default=1)
    def __unicode__(self):
        return self.tnsname
    class Meta:
        app_label='oracle'


class sqlplan(models.Model):
    #ipaddress=models.GenericIPAddressField()
    #tnsname=models.CharField(max_length=50)
    #sql_id=models.CharField(max_length=50)
    child_number=models.BigIntegerField()
    #plan_time=models.BigIntegerField()
    pid=models.BigIntegerField()
    depth=models.BigIntegerField()
    description=models.CharField(max_length=100,null=True)
    object_owner=models.CharField(max_length=65,null=True)
    object_name=models.CharField(max_length=65,null=True)
    object_node=models.CharField(max_length=65,null=True)
    cost=models.CharField(max_length=100,null=True)
    cardinality=models.CharField(max_length=65,null=True)
    bytes=models.CharField(max_length=65,null=True)
    io_cost=models.CharField(max_length=65,null=True)
    #cost=models.BigIntegerField(null=True)
    #cardinality=models.BigIntegerField(null=True)
    #bytes=models.BigIntegerField(null=True)
    #io_cost=models.BigIntegerField(null=True)
    access_predicates=models.CharField(max_length=1000,null=True,default='')
    filter_predicates=models.CharField(max_length=1000,null=True,default='')
    #plan_hash_value=models.CharField(max_length=50)
    def __unicode__(self):
        return self.description
    class Meta:
        app_label='oracle'
