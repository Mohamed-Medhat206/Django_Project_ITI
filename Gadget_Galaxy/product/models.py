from django.db import models

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,null=True)
    slug = models.CharField(max_length=100,null=True)
    description = models.CharField(max_length=9000,null=True)
    price = models.DecimalField(max_digits=10,decimal_places=2,null=True)
    stock = models.IntegerField(null=True)
    sku = models.CharField(max_length=100,null=True)