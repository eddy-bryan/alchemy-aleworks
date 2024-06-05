from django.db import models
import random


class Beer(models.Model):
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    type = models.CharField(max_length=254)
    limited_edition = models.BooleanField()
    description = models.TextField()
    alcohol_content = models.DecimalField(max_digits=2, decimal_places=1)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    @classmethod
    def get_random_beers(cls, limited_edition=False, quantity=1):
        queryset = cls.objects.filter(limited_edition=limited_edition)
        if queryset.exists():
            return random.sample(list(queryset), min(quantity, queryset.count()))
        return None

    def __str__(self):
        return self.name


class MerchItem(models.Model):
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    category = models.CharField(max_length=254)
    description = models.TextField()
    sized_item = models.BooleanField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
