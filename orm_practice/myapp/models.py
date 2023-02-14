from django.db import models

# Create your models here.

class WholeSaleShop(models.Model):
    w_name = models.CharField(max_length=70,null=True, blank=True)
    w_qty = models.IntegerField()

class RetailShop(models.Model):
    r_name = models.CharField(max_length=70,null=True, blank=True)
    r_qty = models.IntegerField()