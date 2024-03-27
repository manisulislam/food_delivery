from django.db import models

# Create your models here.


class Organization(models.Model):
    name = models.CharField(max_length=100,null=True, blank=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    item_type=models.CharField(max_length=20)
    item_description=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.item_type


class Pricing(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    item=models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    zone=models.CharField(max_length=20)
    fixed_price = models.DecimalField(max_digits=10, decimal_places=2,default=10)
    base_distance_in_km = models.IntegerField(default=5)
   

    def __str__(self):
        return self.zone