
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
class danci(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField(default=0)
    def __str__(self):
        return self.name
