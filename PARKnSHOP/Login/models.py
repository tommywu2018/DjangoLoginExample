from __future__ import unicode_literals
import uuid
from django.db import models
from django.contrib import admin

# Create your models here.
class Person(models.Model):
    pkey = models.CharField(max_length=64, default=uuid.uuid4)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    description = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.name

admin.site.register(Person)
