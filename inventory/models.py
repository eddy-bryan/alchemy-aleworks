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
    def get_random_beers(cls, limited_edition=None, quantity=1):
        """
        Retrieve a random sample of beers from the database.

        This method returns a specified number of random Beer objects from the
        database, optionally filtered by whether they are limited edition or not.

        :param limited_edition: Optional boolean value to filter beers.
                                If True, only limited edition beers are returned.
                                If False, only core range beers are returned.
                                If None, no filtering by limited edition status is applied.
                                Defaults to None.
        :param quantity: The number of random Beer objects to retrieve.
                         Defaults to 1. If the quantity requested exceeds the
                         available number of beers, all available beers are returned.
        :return: A list of randomly selected Beer objects. If no beers match the filter,
                 an empty list is returned.
        """
        queryset = cls.objects.all()
        if limited_edition is not None:
            queryset = queryset.filter(limited_edition=limited_edition)
        if queryset.exists():
            return random.sample(list(queryset), min(quantity, queryset.count()))
        return []

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

    @classmethod
    def get_random_merch_items(cls, category=None, quantity=1):
        """
        Retrieve a random sample of merch items from the database.

        This method returns a specified number of random MerchItem objects from the
        database, optionally filtered by category.

        :param category: Optional string to filter merch items by category. 
                         Defaults to None, which means no filtering by category.
        :param quantity: The number of random MerchItem objects to retrieve. 
                         Defaults to 1. If the quantity requested exceeds the 
                         available number of merch items, all available items are returned.
        :return: A list of randomly selected MerchItem objects. If no items match the filter, 
                 None is returned.
        """
        queryset = cls.objects.all()
        if category:
            queryset = queryset.filter(category=category)
        if queryset.exists():
            return random.sample(list(queryset), min(quantity, queryset.count()))
        return None

    def __str__(self):
        return self.name
