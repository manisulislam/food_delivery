from django.db import models

# Create your models here.

ITEMS_TYPE=(
    ('perishable','perishable'),
    ('non-perishable', 'non-perishable'),
)


class Organizaion(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Pricing(models.Model):
    organization = models.ForeignKey(Organizaion, on_delete=models.CASCADE)
    zone=models.CharField(max_length=20)
    fixed_price = models.DecimalField(max_digits=10, decimal_places=2,default=10)
    base_distance_in_km = models.IntegerField(default=10)
    item_type=models.CharField(max_length=20, choices=ITEMS_TYPE, null=True, blank=True)
    item_description=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.item_type