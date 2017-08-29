
from __future__ import unicode_literals

from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    image = models.FileField(upload_to='images/%Y%m%d')