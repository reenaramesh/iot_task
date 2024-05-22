# Create your models here.
from django.db import models


class Device(models.Model):
    device_id = models.IntegerField(blank=True, null=False, primary_key=True)
    device_type = models.CharField(max_length=200,blank=False)
    datetime = models.DateTimeField(auto_now=True)
    data = models.IntegerField(blank=True, null=True)