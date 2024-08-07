import uuid

from decimal import Decimal

from django.db import models
from django.db.models import Sum
from django.conf import settings

from django_countries.fields import CountryField

from inventory.models import Beer, MerchItem
from profiles.models import CustomerProfile


class Order(models.Model):
    """
    Model representing an order placed by a customer.
    """
    order_number = models.CharField(max_length=32, null=False, editable=False)
    customer_profile = models.ForeignKey(CustomerProfile,
                                         on_delete=models.SET_NULL,
                                         null=True, blank=True,
                                         related_name='orders')
    customer_name = models.CharField(max_length=50, null=False, blank=False)
    customer_address1 = models.CharField(max_length=80, null=False,
                                         blank=False)
    customer_address2 = models.CharField(max_length=80, null=True, blank=True)
    customer_city = models.CharField(max_length=40, null=False, blank=False)
    customer_county = models.CharField(max_length=80, null=True, blank=True)
    customer_postcode = models.CharField(max_length=20, null=True, blank=True)
    customer_country = CountryField(blank_label='Country *', null=False,
                                    blank=False)
    customer_email = models.EmailField(max_length=254, null=False, blank=False)
    customer_phone = models.CharField(max_length=20, null=False, blank=False)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_fee = models.DecimalField(max_digits=6, decimal_places=2,
                                       null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False,
                                  default='')

    def _generate_order_number(self):
        """
        Generates a unique, random order number using UUID.
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Updates the order total, delivery fee, and grand total based on line
        items.
        """
        beers = self.beer_line_items.all()
        merch = self.merch_line_items.all()

        self.order_total = (
            sum(Decimal(item.lineitem_total) for item in beers) +
            sum(Decimal(item.lineitem_total) for item in merch) or 0
        )
        if self.order_total < Decimal(settings.FREE_DELIVERY_THRESHOLD):
            self.delivery_fee = Decimal(settings.STANDARD_DELIVERY)
        else:
            self.delivery_fee = Decimal(0)
        self.grand_total = self.order_total + self.delivery_fee
        self.save()

    def save(self, *args, **kwargs):
        """
        Saves the order instance with a generated order number if not already
        set.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Returns a string representation of the order number.
        """
        return self.order_number


class BeerLineItem(models.Model):
    """
    Model representing a line item for beer products within an order.
    """
    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE,
                              related_name='beer_line_items')
    beer = models.ForeignKey(Beer, null=False, blank=False,
                             on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2,
                                         null=False, blank=False,
                                         editable=False)

    def save(self, *args, **kwargs):
        """
        Calculates and saves the total price for the beer line item.
        """
        self.lineitem_total = self.beer.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Returns a string representation of the beer line item.
        """
        return f'Beer {self.beer.name} on order {self.order.order_number}'


class MerchLineItem(models.Model):
    """
    Model representing a line item for merchandise items within an order.
    """
    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE,
                              related_name='merch_line_items')
    merch_item = models.ForeignKey(MerchItem, null=False, blank=False,
                                   on_delete=models.CASCADE)
    merch_item_size = models.CharField(max_length=2, null=True, blank=True)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2,
                                         null=False, blank=False,
                                         editable=False)

    def save(self, *args, **kwargs):
        """
        Calculates and saves the total price for the merchandise line item.
        """
        self.lineitem_total = self.merch_item.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Returns a string representation of the merchandise line item.
        """
        return (
            f'Merch {self.merch_item.name} '
            f'on order {self.order.order_number}'
        )
