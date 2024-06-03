from django.db import models


class Beer(models.Model):
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    type = models.CharField(max_length=254)
    limited_edition = models.BooleanField()
    description = models.TextField()
    alcohol_content = models.DecimalField(max_digits=2, decimal_places=1)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
        